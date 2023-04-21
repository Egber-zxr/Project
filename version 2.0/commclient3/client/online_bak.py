'''
客户机的在线状态
文件的共享托管
获取文件列表
'''
import json

from flask import Flask,send_file,request
from flask import render_template
from client.utils import ConfigUtil

import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    # return "hello World"

@app.route("/getDatas")
def getDatas():
    '''
    获取本客户端的文件及下载路径
    :return:
    '''
    datas = ConfigUtil.read_datas()
    return datas

@app.route("/download1")
def download1():
    '''
    提供文件下载服务
    :return:
    '''
    fileName = request.args.get('fileName')
    filePath = "datas/"+fileName

    # 判断文件是否实际存在，有可能客户端直接删除了实际的文件
    datas = ConfigUtil.read_datas()
    data = datas.split(";")
    flag = False
    for d in data:
        print(d.split("#@#"))
        fn = d.split("#@#")[0]
        if fn==fileName:
            flag = True
            break

    if flag:
        return send_file(filePath, as_attachment=True, attachment_filename=fileName)
    else:
        return "文件没有找到"

@app.route("/files")
def files():
    '''
    提供文件下载服务，即其他客户机下载
    :return:
    '''
    fileName = request.args.get("fileName")
    clientUrl = request.args.get("clientUrl")
    return send_file(clientUrl, fileName, as_attachment=True)

@app.route("/online")
def online():
    '''
    文件在线状态的监听
    :return:
    '''
    return "1"

def sendOnline():
    url = ConfigUtil.read_serverUrl().replace("\"","")+"info/updateOnline"
    clientName = ConfigUtil.read_clientName()
    clientIp = ConfigUtil.read_clientIp()
    headers = {
        'Content-Type': 'application/json',
    }
    data = {'clientName': clientName.replace("\"",""), 'online': "1", 'clientIp': clientIp.replace("\"","")}
    result = requests.post(url, headers=headers, data=json.dumps(data))
    print("上线通知服务器端")

if __name__ == '__main__':
    port = ConfigUtil.read_onlinePort().replace("'","")

    # 上线通知服务器端
    sendOnline()

    app.run(debug=True, port=int(port))

