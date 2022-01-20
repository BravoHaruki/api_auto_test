# -*- coding: utf-8 -*-
# @program: APIAutoTest
# @description: TODO
# @Time : 2022-01-15 21:25
# @Author : Haruki
# @File : html_report.py
# @Version：1.0

import time

from common.log import log
from core.setting_path import DESCRIPTION, HTML_REPORT, RESULT_TITLE, TESTER
from packages.HTMLTestRunner import HTMLTestRunner


def html_report():
    """
    HTML 测试报告
    :return:
    """
    curr_time = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = HTML_REPORT + '/' + RESULT_TITLE + '_' + curr_time + '.html'
    try:
        fp = open(filename, 'wb')
    except Exception as e:
        log.error(f'{filename} 打开失败\n{e}')
        raise e
    else:
        runner = HTMLTestRunner(stream=fp,
                                title=RESULT_TITLE,
                                verbosity=2,
                                tester=TESTER,
                                description=DESCRIPTION)
        log.success('正在使用-html测试报告方式-进行测试')
        return runner, fp, filename
