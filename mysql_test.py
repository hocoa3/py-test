#数据格式:INSERT INTO 表名(字段1,字段2) VALUES (值1,值2)
import os
import re
import time
dir='D:/！已OK/!pic'
info='坊橋夜泊(连接CG写真,很棒)'
my_list='name_list'
column='name,type,my_rank,update_time,now_update'
#value="\'坊橋夜泊\',\'连接CG写真\',\'很棒\',\'2020-12-06\',\'2022-01-17\'"
s_months={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}



txt='C:/Users/86178/Desktop/mysql.txt'
'''
class Teacher(object):
    def __init__(self,name,typee,rank,update_time,now_update):
        self.name=name
        self.typee=typee
        self.rank=rank
        self.update_time=update_time
        self.now_update=now_update
'''


with open(txt,'a+') as f:
#首先从文件夹获取名字,类型,评价
    mode="INSERT INTO %s(%s) VALUES" %(my_list,column)
    tt=(time.ctime().split(' '))
    yearr=tt[4]
    monthh=s_months[tt[1]]
    dayy=tt[2]
    timee=tt[3]
    time_all=(yearr+'-'+monthh+'-'+dayy+' '+timee)
    f.write('%s------------------------------------------------------------------/*\r\n'%(time_all))
    f.write(mode)
    for file in os.listdir(dir):
        name=file.split('(')[0]
        typee=file.split('(')[1].split(',')[0]
        rank=file.split('(')[1].split(',')[1]
        #设置最小与最大时间
        min='2030-12-30'
        max='2010-01-01'
        #进入文件夹获取最大和最小时间来获取何时更新,最新更新
        for file1 in os.listdir(dir+'/'+file):
            #首先获取时间
            time_mode=re.compile(r'\d{4}(-|.)\d{2}(-|.)\d{2}')
            rt=time_mode.search(file1)
            now_time=rt.group()
            if(now_time<min):
                min=now_time
            elif(now_time>max):
                max=now_time
        update_time,now_update=min,max
        #print(typee)
        value="(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" %(name,typee,rank,update_time,now_update)
        f.write(value+',\r\n')
        f.write('\*------------------------------------------------------------------/*\r\n')

print('done')