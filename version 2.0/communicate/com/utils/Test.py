# -*- coding: utf-8 -*-

# 导入必要模块
import pandas as pd
from sqlalchemy import create_engine
from com.config import db_config as dbConfig
db_config = dbConfig.db_config



if __name__ == '__main__':
    engineStr = "mysql+pymysql://"+db_config['username']+":"+db_config['password']+"@"+db_config['host']+":"+str(db_config['port'])+"/"+db_config['database']
    # 初始化数据库连接，使用pymysql模块
    #engine = create_engine('mysql+pymysql://root:root@localhost:3306/flask_base')
    engine = create_engine(engineStr)
    # 读取本地CSV文件
    df = pd.read_csv("E:/python/flask_base/com/utils/companys1.csv", sep=',')

    # 将新建的DataFrame储存为MySQL中的数据表，不储存index列
    df.to_sql('company', engine,if_exists='append',index= False)

    print("写入company表成功!")