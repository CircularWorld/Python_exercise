import pymysql
import re
f = open('dict.txt','r')
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
args_list = []
for line in f:
    pattern = r'(\w+)\s+(.*)'
    res = re.findall(pattern,line)
    args_list.extend(res[0])
try:
        # print(res.group(1),res.group(2))
        sql = "insert into dict (word,mean) values (%s,%s);"
        cur.executemany(sql,args_list)
        db.commit()
except Exception as e:
    print(e)
    db.rollback()


f.close()
cur.close()
db.close()