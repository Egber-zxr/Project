
from flask import session
from flask import request

from com.domain.json_response import JsonResponse

from com.utils import DBUtils as mdb
from flask import current_app

# 初始化所有controller
def init_controller(app):

    # 登录
    @app.route('/login', methods=["POST"])
    def login():
        params = request.json
        sql = "SELECT * FROM  user WHERE userName = %s and password= %s "
        data = (params['userName'],params['password'])
        db = mdb.DBUtils(sql,data)
        rows = db.select()
        if len(rows)>=1:
            session['userId'] = rows[0]['id']
            return JsonResponse.success(rows)
        else:
            return JsonResponse.success(code=-1,msg="用户名或密码错误")


    @app.route('/register', methods=["POST"])
    def register():
        params = request.json
        # 1、 判断用户是否存在
        userExist = check_user_exist(params)
        if userExist:
            return JsonResponse.success("",msg="用户已经存在，请更换用户名")
        # 2、 保存用户
        success = save_user_info(params)
        if success:
            return JsonResponse.success(success,msg="保存成功")
        else:
            return JsonResponse.error("保存失败")

    def check_user_exist(userData):
        sql = "SELECT * FROM  user WHERE userName = %s "
        data = (userData['userName'])
        db = mdb.DBUtils(sql, data)
        rows = db.select()
        if len(rows)>=1:
            return True
        else:
            return False


    # 保存用户数据到数据库
    def save_user_info(userData):

        # SQL插入语句
        sql = "INSERT INTO user(userName,password,name,role)  VALUES('%s','%s','%s','%s')"
        data = (userData['userName'], userData['password'], userData['userName'], "1")
        db = mdb.DBUtils(sql, data)
        resu = db.execute()
        return resu



