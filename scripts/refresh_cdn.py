#!/usr/bin/env python3
import argparse
import base64
import hashlib
import hmac
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timezone


CDN_ENDPOINT = 'https://cdn.aliyuncs.com/'


def percent_encode(value):
    return urllib.parse.quote(str(value), safe='~-._')


def sign_parameters(parameters, access_key_secret, method='GET'):
    canonical_query = '&'.join(
        f'{percent_encode(key)}={percent_encode(parameters[key])}'
        for key in sorted(parameters)
    )
    string_to_sign = f'{method}&%2F&{percent_encode(canonical_query)}'
    digest = hmac.new(
        f'{access_key_secret}&'.encode(),
        string_to_sign.encode(),
        hashlib.sha1,
    ).digest()
    return base64.b64encode(digest).decode()


def build_request(access_key_id, access_key_secret, object_type, object_path):
    parameters = {
        'AccessKeyId': access_key_id,
        'Action': 'RefreshObjectCaches',
        'Format': 'JSON',
        'ObjectPath': object_path,
        'ObjectType': object_type,
        'SignatureMethod': 'HMAC-SHA1',
        'SignatureNonce': str(uuid.uuid4()),
        'SignatureVersion': '1.0',
        'Timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'Version': '2018-05-10',
    }
    parameters['Signature'] = sign_parameters(parameters, access_key_secret, 'POST')
    return urllib.request.Request(
        CDN_ENDPOINT,
        data=urllib.parse.urlencode(parameters).encode(),
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        method='POST',
    )


def refresh_cdn(access_key_id, access_key_secret, object_type, object_path):
    for attempt in range(3):
        try:
            request = build_request(
                access_key_id, access_key_secret, object_type, object_path)
            with urllib.request.urlopen(request, timeout=30) as response:
                result = json.loads(response.read().decode())
            if result.get('Code'):
                raise RuntimeError(
                    f"Aliyun CDN refresh failed: {result['Code']} {result.get('Message', '')}")
            print(
                f"CDN refresh accepted: request_id={result.get('RequestId', '')}, "
                f"task_id={result.get('RefreshTaskId', '')}")
            return
        except (urllib.error.URLError, TimeoutError) as error:
            if attempt == 2:
                raise
            delay = 2 ** attempt
            print(f'CDN refresh request failed, retrying in {delay}s: {error}')
            time.sleep(delay)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', choices=['File', 'Directory'], required=True)
    parser.add_argument('--path', required=True)
    args = parser.parse_args()
    refresh_cdn(
        os.environ['ALIYUN_ACCESS_KEY_ID'],
        os.environ['ALIYUN_ACCESS_KEY_SECRET'],
        args.type,
        args.path,
    )


if __name__ == '__main__':
    main()
