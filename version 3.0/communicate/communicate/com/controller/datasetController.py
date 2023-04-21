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
    @app.route('/dataset/add', methods=["POST"])
    def datasetAdd():
        '''
        新增
        :return:
        '''
        params = request.json
        sql = "INSERT INTO datasets(clientId,fileName)  VALUES('%s','%s')"
        data = (params['clientId'], params['fileName'])
        db = mdb.DBUtils(sql, data)
        resu = db.execute()
        if resu:
            return JsonResponse.success(msg="信息保存成功")
        else:
            return JsonResponse.error(msg="信息保存失败")

    # 查询操作
    @app.route('/dataset/list', methods=["GET"])
    def datasetList():
        '''
        查询
        :return:
        '''
        # params = request.json
        page = request.args.get("page", 1)
        size = request.args.get("size", 100)
        params = {"clientId": request.args.get("clientId", "")}
        sql = "SELECT fileName FROM  datasets WHERE  1=1 "
        sql,data = initParamsData(sql,params)
        db = mdb.DBUtils(sql,data)

        total,rows = db.selectByPage(page, size)

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
