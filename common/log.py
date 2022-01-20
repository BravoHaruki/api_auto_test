# -*- coding: utf-8 -*-
# @program: APIAutoTest
# @description: TODO
# @Time : 2022-01-15 20:57
# @Author : Haruki
# @File : log.py
# @Version：1.0

import os

from loguru import logger

from core.setting_path import LOG_PATH


class Logger:

    @staticmethod
    def log():
        """
        :return: loguru’s logger
        """
        # 判定文件夹
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)

        # 日志文件名称
        log_file = os.path.join(LOG_PATH, "api_test.log")

        # loguru日志
        logger.add(
            log_file,
            level="DEBUG",
            rotation='00:00',
            retention="7 days",
            encoding='utf-8',
            enqueue=True,
            backtrace=True,
            diagnose=True
        )

        return logger


log = Logger().log()
