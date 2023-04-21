import logging
import sys

from flask import Flask,session
from flask import render_template
from flask import request
import json
import pymysql
import uuid

from com.domain.json_response import JsonResponse

from com.utils import DBUtils as mdb
from flask import current_app

# 初始化所有controller
def init_controller(app):
    # 新增操作
    @app.route('/user/add', methods=["POST"])
    def userAdd():
        '''
        新增
        :return:
        '''
        params = request.json
        sql = "INSERT INTO user(userName,password,name,role)  VALUES('%s','%s','%s','%s')"
        data = (params['userName'], params['password'], params['name'], params['role'])
        db = mdb.DBUtils(sql, data)
        resu = db.execute()
        if resu:
            return JsonResponse.success(msg="用户保存成功")
        else:
            return JsonResponse.error(msg="用户保存失败")

    # 删除操作
    @app.route('/user/delete', methods=["POST"])
    def userDelete():
        '''
        删除
        :return:
        '''
        params = request.json
        sql = "DELETE FROM user WHERE id = %s "
        data = (params['id'])
        db = mdb.DBUtils(sql, data)
        resu = db.execute()
        if resu:
            return JsonResponse.success(msg="用户删除成功")
        else:
            return JsonResponse.error(msg="用户删除失败")

    # 修改操作
    @app.route('/user/update', methods=["POST"])
    def userUpdate():
        '''
        修改
        :return:
        '''
        params = request.json
        # SQL插入语句
        sql = "UPDATE user SET userName='%s' , password='%s' , name='%s' , role='%s'  WHERE id = %s "
        data = (params['userName'],params['password'],params['name'],params['role'],params['id'])
        db = mdb.DBUtils(sql, data)
        resu = db.execute()
        if resu:
            return JsonResponse.success(msg="用户修改成功")
        else:
            return JsonResponse.error(msg="用户修改失败")

    # 查询单个实体
    @app.route('/user/detail', methods=["POST"])
    def userDetail():
        '''
        查询单个实体
        :return:
        '''
        params = request.json
        # SQL插入语句
        sql = "SELECT * FROM  user  WHERE id = %s "
        data = (params['id'])
        db = mdb.DBUtils(sql, data)
        rows = db.select()
        if rows:
            return JsonResponse.success(rows[0])
        else:
            return JsonResponse.error(msg="用户获取失败")

    # 查询操作
    @app.route('/user/list', methods=["POST"])
    def userList():
        '''
        查询
        :return:
        '''
        params = request.json
        sql = "SELECT * FROM  user WHERE  1=1 "
        sql,data = initParamsData(sql,params)
        db = mdb.DBUtils(sql,data)
        total,rows = db.selectByPage(params['page'],params['size'])
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
    
