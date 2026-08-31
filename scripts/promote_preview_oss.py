#!/usr/bin/env python3
import argparse
import os
import sys

import oss2


def list_keys(bucket, prefix):
    return [item.key for item in oss2.ObjectIterator(bucket, prefix=prefix)]


def delete_keys(bucket, keys):
    for start in range(0, len(keys), 1000):
        bucket.batch_delete_objects(keys[start:start + 1000])


def copy_prefix(bucket, source_prefix, target_prefix, keys, html_last=False):
    ordered_keys = keys
    if html_last:
        ordered_keys = sorted(keys, key=lambda key: key.lower().endswith(('.html', '.htm')))
    for source_key in ordered_keys:
        relative_key = source_key[len(source_prefix):]
        bucket.copy_object(bucket.bucket_name, source_key, target_prefix + relative_key)


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
    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

    live_prefix = f'preview-{site_name}/'
    staging_prefix = f'_growai_preview_staging/{site_name}/{staging_id}/'
    backup_prefix = f'_growai_preview_backup/{site_name}/{staging_id}/'
    staging_keys = list_keys(bucket, staging_prefix)
    if staging_prefix + 'index.html' not in staging_keys:
        raise RuntimeError('staging preview does not contain index.html')

    live_keys = list_keys(bucket, live_prefix)
    delete_keys(bucket, list_keys(bucket, backup_prefix))
    copy_prefix(bucket, live_prefix, backup_prefix, live_keys)

    try:
        copy_prefix(bucket, staging_prefix, live_prefix, staging_keys, html_last=True)
        expected_live_keys = {live_prefix + key[len(staging_prefix):] for key in staging_keys}
        stale_keys = [key for key in list_keys(bucket, live_prefix) if key not in expected_live_keys]
        delete_keys(bucket, stale_keys)
    except BaseException:
        delete_keys(bucket, list_keys(bucket, live_prefix))
        backup_keys = list_keys(bucket, backup_prefix)
        copy_prefix(bucket, backup_prefix, live_prefix, backup_keys, html_last=True)
        raise
    else:
        delete_keys(bucket, staging_keys)
        delete_keys(bucket, list_keys(bucket, backup_prefix))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f'preview promotion failed: {error}', file=sys.stderr)
        raise
