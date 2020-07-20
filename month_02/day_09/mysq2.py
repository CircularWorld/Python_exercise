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
try:
# name  = input('name:')
# sql = f"select * from cls where name = '{name}';"
# cur.execute(sql)
# sql = f"select * from cls where name = %s or score > %s;"
# cur.execute(sql,[name,80])
# row  =cur.fetchall()
# print(row)
    sql = "insert into cls values(8,'Eva',18,'w',86)"
    cur.execute(sql)
    db.commit() # 提交。将 sql语句的操作行为提交写入数据库
except Exception as e:
    print(e)
    db.rollback() # 没有提交到数据库的内容全部失效，但已经缓存的无法回退，不能完全相信他
cur.close()
db.close()
