# -*- coding: utf-8 -*-
# @program: APIAutoTest
# @description: TODO
# @Time : 2022-01-13 22:33
# @Author : Haruki
# @File : handle_config.py
# @Version：1.0
import configparser


class HandleConfigIni(object):
    def __init__(self):
        """
        :将模块 configparser 实例化为 cf
        """
        self.cf = configparser.ConfigParser()

    def get_conf_value(self, filename, section, name):
        """
        获取文件值
        :param filename:
        :param section:
        :param name:
        :return:
        """
        try:
            self.cf.read(filename, encoding='utf-8')
            value = self.cf.get(section, name)
        except Exception as e:
            print('Read configuration file [%s] about [%s] fail , can not get value' % (filename, section))
            raise e
        else:
            print('Read configuration file [%s] success' % value)
            return value

    def write_conf_value(self, filename, section, name, value):
        """
        写入文件值
        :param filename:
        :param section:
        :param name:
        :param value:
        :return:
        """
        try:
            self.cf.add_section(section)
            self.cf.set(section, name, value)
            self.cf.write(open(filename, 'w', encoding='utf-8'))
        except Exception:
            print('%s 已经存在!' % section)
            raise configparser.DuplicateSectionError(section)
        else:
            print('write these' + section + 'write value' + value + ' success!')
            return value
