# -*- coding:utf-8 -*-
#@Time  : 2019/8/13 11:32
#@Author: csu
#@File  : commonMoudle.py
import os
import readConfig
from xlrd import open_workbook
from xml.etree import ElementTree

localReadconfig = readConfig.ReadConfig()
basePath = readConfig.basePath

class CommonMoudle:
    def __init__(self):
        pass

    def get_excel(self, excel_name, sheet_name):
        cls = []

        excelPath = os.path.join(basePath, 'testData', 'case', excel_name)  #获取用例文件路径
        file = open_workbook(excelPath)
        sheet = file.sheet_by_name(sheet_name)

        '''
        获取sheet内容行数
        如果这个Excel的这个sheet的第i行的第一列不等于case_name那么把这行的数据添加到cls[]
        '''
        nrows = sheet.nrows

        for i in range(nrows):
            if sheet.row_values(i)[0] != u'caseName':
                cls.append(sheet.row_values(i))

        return cls

    '''
    partition() 方法用来根据指定的分隔符将字符串进行分割。

    如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串
    '''
    def get_split(self, responseTxt, leftData, rightData):
        partStr = responseTxt.partition(leftData)
        statusCode = partStr[2].partition(rightData)[0][:]
        return statusCode

    def get_url_from_xml(self, name):

        urlPath = os.path.join(basePath, "testData", "interface", "interfaceURL.xml")
        urlList = []
        tree = ElementTree.parse(urlPath)
        for u in tree.findall('url'):
            url_name = u.get('name')
            if url_name == name:
                for c in u.getchildren():
                    urlList.append(c.text)

        url = '/cloud/common/' + '/'.join(urlList)
        return url

    # ****************************** read SQL xml ********************************
    def get_sql(self, database_name, table_name, sql_id):
        """
        set sql xml
        :return:
        """
        database = {}
        if len(database) == 0:
            sql_path = os.path.join(basePath, "testData", "sql", "SQL.xml")
            tree = ElementTree.parse(sql_path)
            for db in tree.findall("database"):
                db_name = db.get("name")
                # print(db_name)
                table = {}
                for tb in db.getchildren():
                    table_name = tb.get("name")
                    # print(table_name)
                    sql = {}
                    for data in tb.getchildren():
                        sql_id = data.get("id")
                        # print(sql_id)
                        sql[sql_id] = data.text
                    table[table_name] = sql
                database[db_name] = table

        database_dict = database.get(database_name).get(table_name)
        sql = database_dict.get(sql_id)
        return sql

if __name__ == '__main__':
    CommonMoudle = CommonMoudle()
    SQL = CommonMoudle.get_sql('light', 'testtable', 'select_member')
    print(SQL)
