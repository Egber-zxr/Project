import configparser

config_file_url = './config.ini'


def read_downloadPort():
    '''
    读取端口号
    :return:
    '''
    conf = configparser.ConfigParser()
    conf.read(config_file_url,encoding='utf-8')  # 文件名
    return conf.get("global","downloadPort")

def read_serverUrl():
    '''
    读取服务器地址
    :return:
    '''
    conf = configparser.ConfigParser()
    conf.read(config_file_url,encoding='utf-8')  # 文件名
    return conf.get("global","serverUrl")

def read_onlinePort():
    '''
    读取端口号
    :return:
    '''
    conf = configparser.ConfigParser()
    conf.read(config_file_url,encoding='utf-8')  # 文件名
    return conf.get("global","onlinePort")


def read_clientIp():
    '''
    读取终端的IP
    :return:
    '''
    conf = configparser.ConfigParser()
    conf.read(config_file_url,encoding='utf-8')  # 文件名
    return conf.get("global","clientIp")

def read_clientName():
    '''
    读取终端名称
    :return:
    '''
    conf = configparser.ConfigParser()
    conf.read(config_file_url,encoding='utf-8')  # 文件名
    return conf.get("global","clientName")

def read_datas():
    '''
    写入终端已经存储的数据，
    多个数据 用分号 ；分割
    单个数据的名称和下载路径 用 #@# 分割
    :return:
    '''
    conf = configparser.ConfigParser()
    conf.read(config_file_url, encoding='utf-8')  # 文件名
    torchvisonData = conf.get('datas', 'torchvisonData')
    return torchvisonData

def write_datas(torchvisonData):
    '''
    读取终端已经存储的数据，
    多个数据 用分号 ；分割
    单个数据的名称和下载路径 用 #@# 分割
    :return:
    '''
    conf = configparser.ConfigParser()
    conf.set("datas", "torchvisonData", torchvisonData)
    conf.write(open(config_file_url, "w",encoding='utf-8'))

if __name__ == '__main__':
    #读操作
    conf = configparser.ConfigParser()
    conf.read('./../config.ini')     #文件名

    #读取指定的section和name项
    user = conf.get('global', 'user')
    password = conf.get('global', 'password')

    #获取所有的section
    sections = conf.sections()

    torchvisonData = conf.get('datas', 'torchvisonData')
    print(torchvisonData)
    # print(sections)
    # for section in sections:
    #     print(section)
    # 更新指定section, option的值
    # conf.set("section2", "port", "8081")

    # # 添加新的 section
    # conf.add_section("new_section")
    # conf.set("new_section", "new_option", "8000")

    # 写回配置文件
    #conf.write(open("./../config.ini","w"))