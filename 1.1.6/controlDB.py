#-*-coding:utf8-*-
from pymongo import MongoClient
import time
# mongo_uri_auth = 'mongodb://user:password@localhost:27017/'#mongo有要验证的话请自行替换user和password
mongo_uri_no_auth = 'mongodb://localhost:27017/' #mongo没有账号密码验证的时候用这个

client = MongoClient(mongo_uri_no_auth)#创建了与mongodb的连接
db = client.YDY
table = db.t   #获取数据库中表的游标
#你要插入的数据
insert_data = {"name": "Mike", "grade": "two", "age": 12, "sex": "man"}
table.insert_one(insert_data ) #插入一条数据
#查询数据name为Mike的记录
record = table.find_one({"name": "Mike"})
print record

print u'操作数据库完成！'