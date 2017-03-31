#!/usr/bin/python
#coding:utf8

from pymongo import MongoClient  
import sys

#user='root'
#pwd='dYKAMc9K'
#dbname='admin'

user=sys.argv[1]
pwd=sys.argv[2]
dbname=sys.argv[3]
host='172.17.0.165'
port='27017'
uri = 'mongodb://' + user + ':' + pwd + '@' + host + ':' + port +'/'+ dbname

client = MongoClient(uri)











#获取数据库的名字
#db = client.getdatabase(dbname)

#写入数据
#db.collect_name.insert_by(data)

#查询数据
#db.collect_name.find(filter)

