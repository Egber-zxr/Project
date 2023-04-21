from flask import render_template, request
from werkzeug.datastructures import ImmutableMultiDict


def init_routes(app):

    #注册界面
    @app.route('/v_register')
    def register_router():
        return render_template('pages/common/register.html')

    #主页界面
    @app.route('/main')
    def main_router():
        return render_template('pages/common/info.html')

    #用户管理界面
    @app.route('/userManage')
    def userManage_router():
        return render_template('pages/base/userManage.html')

    #公司管理界面
    @app.route('/companyManage')
    def companyManage_router():
        return render_template('pages/busi/companyManage.html')

    # 公司查询界面
    @app.route('/companyList')
    def companyList_router():
        return render_template('pages/busi/companyList.html')

    # 公司地图
    @app.route('/map')
    def map_router():
        params = request.args
        data = ImmutableMultiDict(params).to_dict()
        area = data.get('area')
        result = []
        # return JsonResponse.success(data=result)
        return render_template('pages/busi/map.html',result=result)
