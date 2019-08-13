# -*- coding:utf-8 -*-
#@Time  : 2019/8/13 11:11
#@Author: csu
#@File  : readConfig.py
import os
import  configparser

'''
os.path.realpath: 获取当前文件的全路径
os.path.split：   按照路径将文件名和路径分割开
os.path.join:     将多个路径组合后返回
'''
basePath = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(basePath, 'config.ini')

class ReadConfig:

    def __init__(self):
        self.cf = configparser.ConfigParser()          #类中一个方法 #实例化一个对象
        self.cf.read(configPath, encoding='utf-8')          #read(filename) 读文件config.ini内容

    def get_db(self, param):
        value = self.cf.get('DATABASE', param)
        return value

    def get_http(self, param):
        value = self.cf.get('HTTP', param)
        return value

    def get_email(self, param):
        value = self.cf.get('EMAIL', param)
        return value








