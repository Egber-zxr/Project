'''
主要是下载文件，便于文件的托管
'''
import os

from flask import Flask,send_file,request,send_from_directory
from flask import render_template
from commclient.client.utils import ConfigUtil,TorchvisionUtils,DowloadUtils

import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/files")
def files():
    '''
    提供文件下载服务，即其他客户机下载
    :return:
    '''
    fileName = request.args.get("fileName")
    clientUrl = request.args.get("clientUrl")
    return send_file(clientUrl, fileName, as_attachment=True)

@app.route("/download")
def download():
    '''
    从torchvision下载文件，并将地址传到服务器上
    :return:
    '''

    # fileName = CIFAR10
    fileType = request.args.get("fileType")

    #1、下载数据集
    fileName = TorchvisionUtils.dowloadDatasets(fileType)

    #2、通知服务器端，本地已经存在数据集，并在服务器上注册数据
    url = ConfigUtil.read_serverUrl().replace("\"", "") + "info/addByClient"
    clientName = ConfigUtil.read_clientName()
    clientIp = ConfigUtil.read_clientIp().replace("\"", "")
    onlinePort = ConfigUtil.read_onlinePort().replace("\"", "").replace("'", "")
    clientIp = "http://" + clientIp + ":" + onlinePort + "/online"

    clientUrl = 'C:/Users/dell/Desktop/1.0/commclient/client/datas/'+fileName

    headers = {
        'Content-Type': 'application/json',
    }
    data = {'clientName': clientName.replace("\"", ""), 'online': "1", 'clientIp': clientIp,'clientUrl':clientUrl,'fileName':fileName}
    print(data,url)
    requests.post(url, headers=headers, data=json.dumps(data))

    #3、打开本地文件夹
    # DowloadUtils.openFloder()
    absPath = os.path.abspath('./datas/')
    os.system("explorer.exe %s" % absPath)


    return "成功"

if __name__ == '__main__':
    port = ConfigUtil.read_downloadPort().replace("'","")
    app.run(debug=True, port=int(port))