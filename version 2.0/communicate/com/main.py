'''
@author: My
'''

# 初始化
import time

from flask import Flask
from flask import render_template
import requests
import os
from communicate.com.router import router
from communicate.com.controller import mainController, fileController,baseController,infoController
import logging

from flask_cors import CORS

from communicate.com.domain.json_flask import JsonFlask
from communicate.com.domain.json_response import JsonResponse


# SECRET_KEY
#app = Flask(__name__)
app = JsonFlask(__name__)
CORS(app, supports_credentials=True)
app.config['SECRET_KEY'] = os.urandom(24)

# 文件上传的路径配置
UPLOAD_FOLDER = '../uploadFiles'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 初始化视图
router.init_routes(app)
# 初始化后台请求
mainController.init_controller(app)
# 初始化文件上传
fileController.init_fileController(app)
#
baseController.init_controller(app)
infoController.init_controller(app)

# 设置日志
# 默认日志等级的设置
logging.basicConfig(level=logging.INFO)
formatter = logging.Formatter(
        "[%(asctime)s][%(module)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
log_path = os.path.dirname(os.getcwd()) + '/log/'
log_name = log_path + 'log.log'
handler = logging.FileHandler(log_name, encoding='UTF-8')
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
app.logger.addHandler(handler)



def get_result_json(url):
    try:
        res = requests.get(url)
        res.encoding = 'UTF-8'
    except Exception as e:
        print(e, "网络异常！请检查您的网络！")
        return None
    text = res.text
    return text[46:-14]


# 路由和视图函数
@app.route('/')
def main():
    app.logger.info("开始访问系统！！！！！！")
    return render_template('/pages/main/info.html')


# 启动服务器，默认ip端口为127.0.0.1:8000
if __name__ == '__main__':

    app.run(debug=True,port=8001)