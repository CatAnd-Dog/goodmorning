import pymysql


class user_db():

    # 初始化数据库连接
    # host:数据库地址 user:用户名 port:端口 password:密码 database:数据库名
    def __init__(self, host, user, port, password, database):
        self.db = pymysql.connect(host=host,
                                  user=user,
                                  port=port,
                                  password=password,
                                  database=database,
                                  charset='utf8')
        self.cursor = self.db.cursor()

    # 获取用户数据
    # table_name:表名
    def get_user_msg(self, table_name):
        sql_slect = "SELECT * FROM  {}".format(table_name)
        self.cursor.execute(sql_slect)
        result = self.cursor.fetchall()
        return result

    # 关闭数据库连接
    def shut(self):
        self.cursor.close()
        # 关闭数据库连接
        self.db.close()
