import pymysql
import re

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
    # with open('面向对象.jpg', 'rb') as f:
    #     data = f.read()  # 字节串
    # sql  ='update cls set image = %s where id = 2;'
    # cur.execute(sql,[data])
    # db.commit()
    sql = 'select image from cls where id = 2;'
    cur.execute(sql)
    str = cur.fetchone()
    with open('p.jpg','wb') as f:
        f.write(str[0])
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()
