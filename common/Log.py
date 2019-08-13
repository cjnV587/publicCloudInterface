# -*- coding:utf-8 -*-
#@Time  : 2019/8/13 11:32
#@Author: csu
#@File  : Log.py
import  logging, threading, os
from datetime import datetime
import readConfig

localConfig = readConfig.ReadConfig()

class Log:
    def __init__(self):
        global logPath, resultPath, basePath
        basePath = readConfig.basePath

        resultPath = os.path.join(basePath, 'result')
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)

        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(os.path.join(logPath, "output.log"))      # logging.FileHandler  -> 文件输出
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')    #设置日志格式
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger

    def build_start_line(self, case_no):
        """
        write start line
        :return:
        """
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        """
        write end line
        :return:
        """
        self.logger.info("--------" + case_no + " END--------")

    def build_case_line(self, case_name, code, msg):
        """
        write test case line
        :param case_name:
        :param code:
        :param msg:
        :return:
        """
        self.logger.info(case_name+" - Code:"+code+" - msg:"+msg)

    def get_report_path(self):
        """
        get report file path
        :return:
        """
        report_path = os.path.join(logPath, "report.html")
        return report_path

    def get_result_path(self):
        """
        get test result path
        :return:
        """
        return logPath

    def write_result(self, result):
        """

        :param result:
        :return:
        """
        result_path = os.path.join(logPath, "report.txt")
        fb = open(result_path, "wb")
        try:
            fb.write(result)
        except FileNotFoundError as ex:
            self.logger.error(str(ex))

class MyLog:
    log = None
    mutex = threading.Lock()       #创建锁

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()   #锁定
            MyLog.log = Log()
            MyLog.mutex.release()   #释放

        return MyLog.log