import json
import os
import sys
import unittest
from unittest.mock import MagicMock, patch


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
import refresh_cdn


class Response:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def read(self):
        return json.dumps({'RequestId': 'request', 'RefreshTaskId': 'task'}).encode()


class RefreshCdnTest(unittest.TestCase):
    def test_signature_is_stable_and_uses_rfc3986_encoding(self):
        signature = refresh_cdn.sign_parameters({
            'AccessKeyId': 'testid',
            'Action': 'DescribeRegions',
            'Format': 'XML',
            'SignatureMethod': 'HMAC-SHA1',
            'SignatureNonce': '3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf',
            'SignatureVersion': '1.0',
            'TimeStamp': '2016-02-23T12:46:24Z',
            'Version': '2014-05-26',
        }, 'testsecret')

        self.assertEqual('CT9X0VtwR86fNWSnsc6v8YGOjuE=', signature)

    def test_refresh_calls_aliyun_api(self):
        with patch.object(refresh_cdn.urllib.request, 'urlopen', return_value=Response()) as urlopen:
            refresh_cdn.refresh_cdn('key', 'secret', 'Directory', 'https://preview-a.site.chatai101.com/')

        request = urlopen.call_args.args[0]
        request_body = request.data.decode()
        self.assertEqual('POST', request.method)
        self.assertIn('Action=RefreshObjectCaches', request_body)
        self.assertIn('ObjectType=Directory', request_body)
        self.assertIn('Signature=', request_body)


if __name__ == '__main__':
    unittest.main()
