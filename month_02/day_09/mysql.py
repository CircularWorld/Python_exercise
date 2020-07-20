'''
mysql.py
pymysql
'''
import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu1',
                     charset='utf8'
                     )
# 创建游标 (游标对象负责调用执行sql 语句，操作数据，得到结果)
cur = db.cursor()

# # 对数据库操作 增删改查
# sql = 'select name,age,score from cls;'
# cur.execute(sql)  # 执行sql语句
#获取一条
# row  = cur.fetchone()
# 从第一个基础上取 类似文件读
# row  = cur.fetchmany(2)
# 多个结果 没有返回 （）
# row  = cur.fetchall()

# cur 在查询后可以迭代取值
# for row in cur:
#     print(row)
# 关闭游标 和数据库


cur.close()
db.close()
