#!/usr/bin/env python3

import json

import requests


class Remote:

    def __init__(self):
        pass

    def get_products(self,provider,service,region):
        return json.loads(requests.get(f'http://127.0.0.1:8000/api/v1/providers/{provider}/services/{service}/regions/{region}/products').text)


if __name__ == '__main__':
    from pprint import pprint

    remote = Remote()
    pprint(remote.get_products('amazon','compute','us-east-1'))
