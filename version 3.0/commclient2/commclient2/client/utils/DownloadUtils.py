# -*- coding:utf-8 -*-
import requests
import time
import os

data_folder_path = "./datas/"


# 当把get函数的stream参数设置成False时，
# 它会立即开始下载文件并放到内存中，如果文件过大，有可能导致内存不足。
def downloadByUrl(url, fileName):
    # 当把get函数的stream参数设置成True时，它不会立即开始下载，
    # 使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载
    r = requests.get(url, stream=True)
    f = open(data_folder_path+fileName, "wb")
    realpath = os.path.realpath(data_folder_path)
    start = time.time()
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
            f.flush()
    # iter_content：一块一块的遍历要下载的内容
    # iter_lines：一行一行的遍历要下载的内容
    # 这两个函数下载大文件可以防止占用过多的内存，因为每次只下载小部分数据
    end = time.time()
    print('文件下载完毕！耗时：', end - start)
    os.system("explorer.exe %s" % realpath)

def openFolder():
    '''
    打开本地文件夹
    :return:
    '''
    os.system("explorer.exe %s" % data_floder_path)


if __name__ == '__main__':
    downloadByUrl("http://127.0.0.1:8101/download","data.txt")