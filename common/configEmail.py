# -*- coding:utf-8 -*-
#@Time  : 2019/4/11 17:18
#@Author: junni
#@File  : configEmail.py
import os
import readConfig
import datetime
import win32com.client as win32
from common.Log import MyLog

localReadConfig = readConfig.ReadConfig()
proDir = readConfig.basePath

class send_email:
    def __init__(self):
        global subject, app, addressee, cc, mail_path
        self.subject = localReadConfig.get_email("subject")
        self.app = localReadConfig.get_email("app")
        self.addressee = localReadConfig.get_email("addressee")
        self.cc = localReadConfig.get_email("cc")

        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        #self.mail_path = os.path.join(proDir, 'result', 'report.html')
        self.mail_path = MyLog.get_log().get_report_path()

    def outlook(self):
        olook = win32.Dispatch("%s.application" % self.app)  #固定写法
        mail = olook.CreateItem(0)                           #固定写法
        mail.To = self.addressee      #收件人
        mail.CC = self.cc             #抄送人
        mail.Subject = str(datetime.datetime.now())[0:19] + '测试报告'  # 邮件主题
        mail.Attachments.Add(self.mail_path, 1, 1, "myFile")
        read = open(self.mail_path, encoding='utf-8')  # 打开需要发送的测试报告附件文件
        content = read.read()  # 读取测试报告文件中的内容
        read.close()
        #mail.Body = content  # 将从报告中读取的内容，作为邮件正文中的内容
        mail.Body = '接口测试结果'
        mail.Send()  # 发送

if __name__ == '__main__':  # 运营此文件来验证写的send_email是否正确
    print(send_email().subject)
    send_email().outlook()
    print("send email ok!!!!!!!!!!")


