#!/usr/bin/env python3
import argparse
import os
import sys
import time

import oss2


MAX_ATTEMPTS = 5


def log(message):
    print(message, flush=True)


def retry(operation, description):
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            return operation()
        except Exception as error:
            if attempt == MAX_ATTEMPTS:
                log(f'{description} failed after {attempt} attempts: {error}')
                raise
            delay = min(2 ** attempt, 15)
            log(f'{description} failed ({attempt}/{MAX_ATTEMPTS}): {error}; retrying in {delay}s')
            time.sleep(delay)


def list_keys(bucket, prefix):
    keys = retry(
        lambda: [item.key for item in oss2.ObjectIterator(bucket, prefix=prefix)],
        f'list {prefix}'
    )
    log(f'listed {len(keys)} objects from {prefix}')
    return keys


def delete_keys(bucket, keys):
    for start in range(0, len(keys), 1000):
        batch = keys[start:start + 1000]
        retry(lambda: bucket.batch_delete_objects(batch), f'delete {len(batch)} objects')
        log(f'deleted {min(start + len(batch), len(keys))}/{len(keys)} objects')


def copy_prefix(bucket, source_prefix, target_prefix, keys, html_last=False):
    ordered_keys = keys
    if html_last:
        ordered_keys = sorted(keys, key=lambda key: key.lower().endswith(('.html', '.htm')))
    total = len(ordered_keys)
    for index, source_key in enumerate(ordered_keys, 1):
        relative_key = source_key[len(source_prefix):]
        target_key = target_prefix + relative_key
        retry(
            lambda: bucket.copy_object(bucket.bucket_name, source_key, target_key),
            f'copy {source_key} to {target_key}'
        )
        if index == total or index % 50 == 0:
            log(f'copied {index}/{total} objects from {source_prefix} to {target_prefix}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--site-name', required=True)
    parser.add_argument('--staging-id', required=True)
    args = parser.parse_args()

    site_name = args.site_name
    staging_id = args.staging_id
    if not site_name or any(char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-' for char in site_name):
        raise ValueError('invalid site name')
    if not staging_id or any(char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.' for char in staging_id):
        raise ValueError('invalid staging id')

    endpoint = os.environ['ALIYUN_OSS_ENDPOINT']
    if not endpoint.startswith(('http://', 'https://')):
        endpoint = 'https://' + endpoint
    access_key_id = os.environ['ALIYUN_ACCESS_KEY_ID']
    access_key_secret = os.environ['ALIYUN_ACCESS_KEY_SECRET']
    bucket_name = os.environ.get('ALIYUN_OSS_BUCKET', 'grow-ai-sites')
    bucket = oss2.Bucket(
        oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name,
        connect_timeout=30
    )

    live_prefix = f'preview-{site_name}/'
    staging_prefix = f'_growai_preview_staging/{site_name}/{staging_id}/'
    backup_prefix = f'_growai_preview_backup/{site_name}/{staging_id}/'
    staging_keys = list_keys(bucket, staging_prefix)
    if staging_prefix + 'index.html' not in staging_keys:
        raise RuntimeError('staging preview does not contain index.html')

    log(f'promoting {len(staging_keys)} staging objects to {live_prefix}')
    live_keys = list_keys(bucket, live_prefix)
    delete_keys(bucket, list_keys(bucket, backup_prefix))
    log(f'backing up {len(live_keys)} live objects')
    copy_prefix(bucket, live_prefix, backup_prefix, live_keys)

    try:
        log('copying staging objects to live preview')
        copy_prefix(bucket, staging_prefix, live_prefix, staging_keys, html_last=True)
        expected_live_keys = {live_prefix + key[len(staging_prefix):] for key in staging_keys}
        stale_keys = [key for key in list_keys(bucket, live_prefix) if key not in expected_live_keys]
        log(f'deleting {len(stale_keys)} stale live objects')
        delete_keys(bucket, stale_keys)
    except BaseException:
        log('promotion failed; restoring previous live preview')
        delete_keys(bucket, list_keys(bucket, live_prefix))
        backup_keys = list_keys(bucket, backup_prefix)
        copy_prefix(bucket, backup_prefix, live_prefix, backup_keys, html_last=True)
        raise
    else:
        log('promotion succeeded; cleaning staging and backup objects')
        delete_keys(bucket, staging_keys)
        delete_keys(bucket, list_keys(bucket, backup_prefix))
        log('preview promotion completed')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f'preview promotion failed: {error}', file=sys.stderr)
        raise
