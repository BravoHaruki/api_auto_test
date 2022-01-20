# -*- coding: utf-8 -*-
# @Time : 2022/1/7 11:29
# @Author : Haruki
# @File : RequestUtil.py
import requests


class RequestUtil:

    def __init__(self):
        pass

    def request(self, url, method, headers=None, param=None, content_type=None):
        """
        Http request common method
        :param url:
        :param method:
        :param headers:
        :param param:
        :param content_type:
        :return:
        """
        try:
            if method == "get":
                result = requests.get(url=url, params=param, headers=headers).json()
                return result

            elif method == "post":
                if content_type == "application/json":
                    result = requests.post(url=url, json=param, headers=headers).json()
                    return result
                elif content_type == "application/x-www-form-urlencoded":
                    result = requests.post(url=url, data=param, headers=headers).json()
                    return result
            else:
                print("HTTP Method is not allowed")

        except Exception as e:
            print("HTTP Request Error:{0}".format(e))
