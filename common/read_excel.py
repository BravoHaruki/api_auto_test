# -*- coding: utf-8 -*-
# @Time : 2022/1/13 10:13
# @Author : Haruki
# @File : read_excel.py
import os.path

import xlrd

from common import log
from core.setting_path import XLSX_FILE


class ReadExcel:
    def __init__(self, fileName, sheetName="API_TEST_DATA"):
        """
        :param fileName:
        :param sheetName:
        """
        file = os.path.join(XLSX_FILE, fileName)
        self.data = xlrd.open_workbook(file)
        self.table = self.data.sheet_by_name(sheetName)
        self.rows = self.table.nrows
        self.clos = self.table.ncols


    def read_data(self):
        """
        :return: 文件数据
        """
        if self.rows > 1:
            # 获取第一行的内容，列表格式
            keys = self.table.row_values(0)
            data_list = []
            # 获取每一行的内容，列表格式
            for col in range(1, self.rows):
                values = self.table.row_values(col)
                # keys，values组合转换为字典
                api_dict = dict(zip(keys, values))
                data_list.append(api_dict)
            return data_list
        else:
            log.warning("数据表格没有数据!")
            return None
