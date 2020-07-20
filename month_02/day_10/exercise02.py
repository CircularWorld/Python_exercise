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
l = [('小李',14,'60'),('小王',15,'66')]
try:
    sql = ("insert into cls (name,age,score) values (%s,%s,%s);")

    cur.executemany(sql,[('小李',14,'60'),('小王',15,'66')])
    db.commit()
except Exception as e:
    print(e)
    db.rollback()



cur.close()
db.close()



