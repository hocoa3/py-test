#数据格式:INSERT INTO 表名(字段1,字段2) VALUES (值1,值2)
import os
import re

info='坊橋夜泊(连接CG写真,很棒)'
my_list='name_list'
column='name,type,my_rank,update_time,now_update'
value="\'坊橋夜泊\',\'连接CG写真\',\'很棒\',\'2020-12-06\',\'2022-01-17\'"

print(value)
mode="INSERT INTO %s(%s) VALUES(%s)" %(my_list,column,value)
txt='C:/Users/86178/Desktop/mysql.txt'
with open(txt,'w') as f:
    f.write(mode)

print('done')