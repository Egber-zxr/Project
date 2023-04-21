import pymysql
import logging
import sys
from com.config import db_config as dbConfig

# 加入日志
# 获取logger实例
logger = logging.getLogger("baseSpider")
# 指定输出格式
formatter = logging.Formatter('%(asctime)s\
              %(levelname)-8s:%(message)s')
# 文件日志
file_handler = logging.FileHandler("operation_database.log")
file_handler.setFormatter(formatter)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# 为logge添加具体的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)

db_config = dbConfig.db_config


class DBUtils():
    # 构造函数,初始化数据库连接
    def __init__(self,sql,params=None):
        self.sql = sql
        self.params = params
        self.conn = None
        self.cur = None

    def connectiondatabase(self):
        try:
            self.conn = pymysql.connect(host=db_config['host'],user=db_config['username'],
                                    password=db_config['password'],database=db_config['database'],charset=db_config['charset'])
        except:
            logger.error("connectDatabase failed")
            return False
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        return True

    # 关闭数据库
    def closedatabase(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self):
        self.connectiondatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                logger.info(self.sql % self.params)
                self.cur.execute(self.sql % self.params)
                self.conn.commit()
        except:
            logger.error("execute failed: " + self.sql)
            logger.error("params: " + self.params)
            self.closedatabase()
            return False
        return True

    # 用来查询表数据
    def select(self):
        self.connectiondatabase()
        self.cur.execute(self.sql,self.params)
        result = self.cur.fetchall()
        return result

    # 用来查询表数据
    def selectByPage(self,page,size):
        self.connectiondatabase()

        self.cur.execute(self.sql, self.params)
        allResult = self.cur.fetchall()
        total = len(allResult)

        limitSql= self.sql + "limit %s,%s"
        limitParams = self.params +((page-1)*size,size,)
        #print(limitSql % limitParams)
        self.cur.execute(limitSql, limitParams)
        rows = self.cur.fetchall()
        return total,rows