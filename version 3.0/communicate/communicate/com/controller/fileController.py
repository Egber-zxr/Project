import os
import json

from flask import request, make_response
from projects.communicate.communicate.com.utils import StringUtils


basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])

# 检验图片的正确性
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#初始化文件请求路由
def init_fileController(app):
    # 上传文件
    @app.route('/uploadFile', methods=['POST'], strict_slashes=False)
    def api_upload():
        file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        f = request.files['file']
        if f and allowed_file(f.filename):
            fname = f.filename
            print(file_dir+fname)
            ext = fname.rsplit('.', 1)[1]
            new_filename = StringUtils.createUUID() + '.' + ext
            f.save(os.path.join(file_dir, new_filename))

            resu = {}
            resu['code'] = 0;
            resu['msg'] = "上传成功";
            resu['fileName'] = new_filename;
            return json.dumps(resu, ensure_ascii=False)
        else:
            resu = {}
            resu['code'] = 0;
            resu['msg'] = "上传失败";
            resu['fileName'] = "/upload/error.png";
            return json.dumps(resu, ensure_ascii=False)

    # 回显图片
    @app.route('/images/<string:filename>', methods=['GET'])
    def show_images(filename):
        file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
        if request.method == 'GET':
            if filename is None:
                pass
            else:
                image_data = open(os.path.join(file_dir, '%s' % filename), "rb").read()
                response = make_response(image_data)
                response.headers['Content-Type'] = 'image/png'
                return response
        else:
            pass

    # 查询客户端数据集
