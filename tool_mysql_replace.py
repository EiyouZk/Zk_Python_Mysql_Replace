#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# �����ݿ�����
db = MySQLdb.connect("localhost","root","root","jls_imgbook2" )

# ʹ��cursor()������ȡ�����α� 
cursor = db.cursor()

# SQL �������
id = 25160
orderid = 157997
for i in range(1,115):
	chap = "44_1474189211_"+str(id)
	sql = "INSERT INTO _t_md_mddata_comparison(_id,_comparison_table,_comparison_idx,\
	      _attribute_idx,_attribute,_link_table,_remark,_userstamp) \
	      VALUES ('%d','%s', '%s', '%s', '%s', '%s' , '%s' , '%s' )" % \
	      (orderid+i, '', chap, '43_8888_763',"","_t_md_mddata","", "2_1473840341_8")

	try:
	   # ִ��sql���
	   cursor.execute(sql)
	   # �ύ�����ݿ�ִ��
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()
	id += 1

# �ر����ݿ�����
db.close()