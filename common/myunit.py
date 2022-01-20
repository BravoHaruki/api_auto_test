# -*- coding: utf-8 -*-
# @program: APIAutoTest
# @description: TODO
# @Time : 2022-01-15 21:43
# @Author : Haruki
# @File : myunit.py
# @Version：1.0

import unittest

import requests

from common.log import log
from common.read_yaml import ReadYaml

requestInfo = ReadYaml().read_yaml('get_token.yaml')['login']


class MyUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        url = requestInfo['url']
        data = requestInfo['data']
        headers = requestInfo['headers']
        try:
            response = requests.post(url=url, data=data, headers=headers).json()['data']
        except Exception as e:
            log.warning(f'获取 token 失败，如果你不需要 token 忽略即可\n{e}')
        # 全局变量token
        global token
        token = response['token']
        log.info(f'获取全局 token 成功: {token}')

    def setUp(self) -> None:
        log.info('new test start')

    def tearDown(self) -> None:
        log.info('this test end')

    @classmethod
    def tearDownClass(cls) -> None:
        log.info('全部测试执行完毕')
