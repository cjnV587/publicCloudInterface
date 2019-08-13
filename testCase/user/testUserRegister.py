# -*- coding:utf-8 -*-
#@Time  : 2019/8/13 11:46
#@Author: csu
#@File  : testUserRegister.py
import unittest
from common import configHttp
from common import Log as Log
from common import commonMoudle
import paramunittest

localConfigHttp = configHttp.ConfigHttp()
localcommonMoudle =commonMoudle.CommonMoudle()

userRegister_xls = localcommonMoudle.get_excel("userCase.xlsx", "userRegister")
@paramunittest.parametrized(*userRegister_xls)
class testUserRegister(unittest.TestCase):
    def setParameters(self, caseName, request, result, statusCode, statusString):

        self.caseName = str(caseName)
        self.request = str(request)
        self.result = str(result)
        self.statusCode = str(statusCode)
        self.statusString = str(statusString)
        self.return_xml = None
        self.info  = None

    def description(self):
        """
        test report description
        :return:
        """
        self.caseName

    def setUp(self):
        """

        :return:
        """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.caseName)


    def testUserRegister(self):
        u''': 2.2APP请求进行用户注册接口测试用例'''           # 说明测试用例的标题

        # set url
        self.set_url = localcommonMoudle.get_url_from_xml('userRegister')
        localConfigHttp.set_url(self.set_url)
        print("第一步：设置url：  "+self.set_url)

        # set params
        localConfigHttp.set_data(self.request)
        print("第二步：设置发送请求的参数： %s" % self.request)

        # test interface
        self.return_xml = localConfigHttp.post()
        print("第三步：发送请求，获取响应结果： %s" % self.return_xml.text)

        # check result
        self.checkResult()
        print("第五步：检查结果")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        self.info = self.return_xml.text
        code = localcommonMoudle.get_split(self.info, '<statusCode>', '</statusCode>')
        statusStr = localcommonMoudle.get_split(self.info, '<statusString>', '</statusString>')

        if self.result == '0':
            self.assertEqual(code, self.statusCode)
            self.assertEqual(statusStr, self.statusString)


