# -*- coding: UTF-8 -*-
# @author: admin
# @createTime: 2022/7/25 11:43 
# @description:
from os.path import realpath, dirname
import json


def get_config(name: str):
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
