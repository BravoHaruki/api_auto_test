# -*- coding: utf-8 -*-
# @program: APIAutoTest
# @description: TODO
# @Time : 2022-01-15 21:48
# @Author : Haruki
# @File : RunAllCases.py
# @Version：1.0

import unittest
from unittest import runner

from common.html_report import html_report
from common.log import log
from core.setting_path import TEST_CASES

if __name__ == '__main__':
    try:
        '''
		HTMLTestRunner Test Report
		'''
        test_suite = unittest.defaultTestLoader.discover(TEST_CASES, 'test*.py')
        runner, fp, fileName = html_report()
        runner.run(test_suite)
    except Exception as e:
        log.error('运行出错！！！请检查！！！')
        raise e
