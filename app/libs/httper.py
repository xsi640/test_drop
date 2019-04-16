# coding: utf-8
'''
author: suyang
'''
import requests

__author__ = 'suyang'


def get(url, is_json=True):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json() if is_json else r.text
    else:
        return {} if is_json else ''
