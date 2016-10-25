#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","jls_imgbook2" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
id = 25160
orderid = 157997
for i in range(1,115):
	chap = "44_1474189211_"+str(id)
	sql = "INSERT INTO _t_md_mddata_comparison(_id,_comparison_table,_comparison_idx,\
	      _attribute_idx,_attribute,_link_table,_remark,_userstamp) \
	      VALUES ('%d','%s', '%s', '%s', '%s', '%s' , '%s' , '%s' )" % \
	      (orderid+i, '', chap, '43_8888_763',"","_t_md_mddata","", "2_1473840341_8")

	try:
	   # 执行sql语句
	   cursor.execute(sql)
	   # 提交到数据库执行
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()
	id += 1

# 关闭数据库连接
db.close()