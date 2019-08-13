# -*- coding:utf-8 -*-
#@Time  : 2019/8/12 19:57
#@Author: csu
#@File  : configHttp.py
import requests
from common.Log import MyLog as Log
import readConfig

localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        global protocol, ip, port
        protocol = localReadConfig.get_http('protocol')
        ip = localReadConfig.get_http('ip')
        port = localReadConfig.get_http('port')

        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.data = None
        self.url = None

    def set_url(self, url):
        self.url = protocol + '://' + ip + ':' + port + url
        return self.url

    def set_data(self, data):
        self.data = data
        return self.data

    def get(self):
        response = requests.get(self.url)
        return response

    def post(self):
        response = requests.post(self.url, data = self.data)
        return response




