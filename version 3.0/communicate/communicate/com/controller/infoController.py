import logging
import sys

import requests
from flask import Flask,session
from flask import render_template
from flask import request
import json
import pymysql
import uuid

from projects.communicate.communicate.com.domain.json_response import JsonResponse

from projects.communicate.communicate.com.utils import DBUtils as mdb
from flask import current_app

# 初始化所有controller
def init_controller(app):
    # 新增操作
    @app.route('/info/add', methods=["POST"])
    def infoAdd():
        '''
        新增
        :return:
        '''
        params = request.json
        sql = "INSERT INTO info(clientName,fileName,orgUrl,clientUrl,online)  VALUES('%s','%s','%s','%s','%s')"
        data = (params['clientName'], params['fileName'], params['orgUrl'], params['clientUrl'], params['online'])
        db = mdb.DBUtils(sql, data)
        resu = db.execute()
        if resu:
            return JsonResponse.success(msg="信息保存成功")
        else:
            return JsonResponse.error(msg="信息保存失败")

    # 删除操作
    @app.route('/info/delete', methods=["POST"])
    def infoDelete():
        '''
        删除
        :return:
        '''
        params = request.json
        sql = "DELETE FROM info WHERE id = %s "
        data = (params['id'])
        db = mdb.DBUtils(sql, data)
        resu = db.execute()
        if resu:
            return JsonResponse.success(msg="信息删除成功")
        else:
            return JsonResponse.error(msg="信息删除失败")

    # 修改操作
    @app.route('/info/update', methods=["POST"])
    def infoUpdate():
        '''
        修改
        :return:
        '''
        params = request.json
        # SQL插入语句
        sql = "UPDATE info SET clientName='%s' , fileName='%s' , orgUrl='%s' , clientUrl='%s' , online='%s'  WHERE id = %s "
        data = (params['clientName'],params['fileName'],params['orgUrl'],params['clientUrl'],params['online'],params['id'])
        db = mdb.DBUtils(sql, data)
        resu = db.execute()
        if resu:
            return JsonResponse.success(msg="信息修改成功")
        else:
            return JsonResponse.error(msg="信息修改失败")

    # 查询单个实体
    @app.route('/info/detail', methods=["POST"])
    def infoDetail():
        '''
        查询单个实体
        :return:
        '''
        params = request.json
        # SQL插入语句
        sql = "SELECT * FROM  info  WHERE id = %s "
        data = (params['id'])
        db = mdb.DBUtils(sql, data)
        rows = db.select()
        if rows:
            return JsonResponse.success(rows[0])
        else:
            return JsonResponse.error(msg="信息获取失败")

    # 查询操作
    @app.route('/info/list', methods=["POST"])
    def infoList():
        '''
        查询
        :return:
        '''
        params = request.json
        sql = "SELECT * FROM  info WHERE  1=1 "
        sql,data = initParamsData(sql,params)
        db = mdb.DBUtils(sql,data)

        total,rows = db.selectByPage(params['page'],params['size'])

        # 查询的时候要监测下客户端是否在线
        # for row in rows:
        #     url = row['clientIp']
        #     online = '1'
        #     if not checkOnline(url):
        #         online = '0'
        #     sql1 = "UPDATE info SET online='%s' WHERE id = %s"
        #     data1 = (online, row['id'])
        #     print(data)
        #     db1 = mdb.DBUtils(sql1, data1)
        #     resu = db1.execute()

        total, rows = db.selectByPage(params['page'], params['size'])
        result={
            'total':total,
            "list":rows
        }
        return JsonResponse.success(result)


    def initParamsData(sql,params):
        '''
        格式化查询参数
        :param sql:
        :param params:
        :return:
        '''
        data = ()
        for (key,value) in params.items():
            if key=='page' or key=='size':
                continue
            if value!='':
                sql += " AND "+key+" like %s "
                data = data+('%'+value+'%',)
        return sql,data

    # 查询操作
    @app.route('/info/downloadlist', methods=["POST"])
    def downloadlist():
        '''
        查询
        :return:
        '''
        params = request.json
        sql = "SELECT id, clientName, (SELECT GROUP_CONCAT(fileName) FROM datasets WHERE clientId = info.id) AS " \
              "datasetFileNames, fileName, orgUrl, clientUrl, online, clientIp, last_online FROM  info WHERE  1=1 "
        sql, data = initParamsData(sql, params)
        db = mdb.DBUtils(sql, data)
        total, rows = db.selectByPage(params['page'], params['size'])

        # 查询的时候要监测下客户端是否在线
        # for row in rows:
        #     url= row['clientIp']
        #     online = '1'
        #     if not checkOnline(url):
        #         online = '0'
        #     sql1 = "UPDATE info SET online='%s' WHERE id = %s"
        #     data1 = (online, row['id'])
        #     print(data)
        #     db1 = mdb.DBUtils(sql1, data1)
        #     resu = db1.execute()

        total, rows = db.selectByPage(params['page'], params['size'])
        result = {
            'total': total,
            "list": rows
        }
        return JsonResponse.success(result)

    def checkOnline(url):
        '''
        检查客户端是否在线
        :param url:
        :return:
        '''
        headers = {
            'Content-Type': 'application/json',
        }
        data = {}
        try:
            result = requests.get(url, headers=headers, data=json.dumps(data))
            print(result)
            if result.content.decode('UTF-8')=='1':
                return True
            else:
                return False
        except:
            return False

    # 修改操作
    @app.route('/info/updateOnline', methods=["POST"])
    def infoUpdateOnline():
        '''
        修改
        :return:
        '''
        params = request.json
        print(params)
        # SQL插入语句
        sql = "UPDATE info SET online='%s',clientIp='%s', last_online=now()  WHERE clientName = '%s'"

        data = (params['online'],params['clientIp'],params['clientName'])
        print(data)
        db = mdb.DBUtils(sql, data)
        resu = db.execute()
        if resu:
            return JsonResponse.success(msg="信息修改成功")
        else:
            return JsonResponse.error(msg="信息修改失败")

    # 查询客户端在线情况
    @app.route('/info/checkOnline', methods=["GET"])
    def infoCheckOnline():
        '''
        查询
        :return:
        '''
        # SQL查询语句
        sql = "select clientName from info where online = '1'"
        db = mdb.DBUtils(sql)
        rows = db.select()
        clients = [item.get('clientName') for item in rows]
        if clients:
            return JsonResponse.success(clients)
        else:
            return JsonResponse.error(msg="没有数据")

    # 新增操作
    @app.route('/info/addByClient', methods=["POST"])
    def addByClient():
        '''
        新增
        :return:
        '''
        params = request.json
        print(params)
        sql = "INSERT INTO info(clientName,fileName,clientUrl,online,clientIp)  VALUES('%s','%s','%s','%s','%s')"
        data = (params['clientName'], params['fileName'], params['clientUrl'], params['online'], params['clientIp'])
        db = mdb.DBUtils(sql, data)
        resu = db.execute()
        if resu:
            return JsonResponse.success(msg="信息保存成功")
        else:
            return JsonResponse.error(msg="信息保存失败")
