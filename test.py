import re
import os 
import os.path
from functools import reduce
import functools
import time
import pHash
import random

import numpy as np
import cv2
dir=r'D:\幼井作品合集\幼井'
dir1=(r'C:\Users\86178\BaiduNetDisk\こんな幼馴染がいてほしい\Fanbox\幼馴染系列')
save_path=r'D:/Nahaki(插画,很棒，等待更新)#21.10'
dir=dir.replace('\\','/')                             #将地址转义
save_path=save_path.replace('\\','/')
flag=1
#flag=1时为test,2为Bring_all,3为Keep_name,4为相互比较文件
                                                        #str->float
def metric(func):                                                          
    @functools.wraps(func)
    def wrapper(*args,**kw):
        f1=time.time()
        res=func(*args,**kw)
        f2=time.time()
        print('%s executed in %.1fs ' % (func.__name__,float(f2-f1)))
        return res
    return wrapper

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('%s executed in %s-%s-%s %s:%s:%s ' % (func.__name__, time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday,time.localtime().tm_hour,time.localtime().tm_min,time.localtime().tm_sec))
        return func
    return wrapper

def Date_Generator(n):
  while(n>0):
    year=random.randint(2020,2022)   
    month=random.randint(1,12)
    day=random.randint(1,31)
    yield year,month,day
    n=n-1
'''#使用案例
for x in Date_Generator(50):
    name=("%d-%02d-%02d " % (x[0],x[1],x[2]))
    print(name)
    if(not os.path.exists(dir+'/'+name)):
      os.mkdir(dir+'/'+name)
'''
@metric
def test(dir,save_path):
  print('1')
  '''                         #根据文件创建日期来修改名字
  for file in os.listdir(dir):
    if(os.path.isdir(dir+'/'+file)):
      for file1 in os.listdir(dir+'/'+file):
        m_time=os.path.getmtime(dir+'/'+file+'/'+file1)
        t_time=time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(m_time))
        if(os.path.exists(dir+'/'+file+'/'+t_time+file1[-4:])):
          print(dir+'/'+file+'/'+file1)
        else:
          os.rename(dir+'/'+file+'/'+file1,dir+'/'+file+'/'+t_time+file1[-4:])
  '''
  '''
  for name in os.listdir(dir):                            #删除固定页数以外的其他所有
    dir1=dir+'/'+name
    print(dir1)         
                                                     
    sta=input("开始")
    if(sta=='p'):
      continue
    elif(sta=='done'):
      break
    sta1=int(sta)-1
    end=input("结束")
    end1=int(end)+1
    num=len(os.listdir(dir1))
    print(num)
    while(sta1>0 or end1<(num+1)):
      if(os.path.exists(dir1+'/'+str(sta1)+'.jpeg')):
        os.remove(dir1+'/'+str(sta1)+'.jpeg')
        print('remove1' +dir1+str(sta1)+'.jpeg')
        sta1=sta1-1
      else:
        sta1=sta1-1
        if(sta1<-400):
          break
      if(os.path.exists(dir1+'/'+str(end1)+'.jpeg')):
        os.remove(dir1+'/'+str(end1)+'.jpeg')
        print('remove2' +dir1+'/'+str(end1)+'.jpeg')
        end1=end1+1
  '''
  ''' 
  idx=s.index('.')                                          #索引目标位置
  p1=reduce(big,map(str2int,s[:idx]))+(reduce(small,map(str2int,s[idx+1:]))/10**len(s[idx+1:]))
  return p1
  '''                                                                 
  '''                                                     #杨辉三角
  L=[1]                                                    #a[::-1]字符串倒写
  yield L
  L=[1,1]
  while (n-1)>0:
    yield L
    n=n-1
    L=[1]+ [L[i]+L[i+1] for i in range(len(L)-1)] + [1]     #[]+[]可以把列表连接起来
  '''    
  '''
  for file in os.listdir(dir):                                #为文件添加前缀
    os.rename(dir+'/'+file,dir+'/pixiv-'+file)
  '''
  '''
  for file in os.listdir(dir):                                #../2，把2里的文件提取出来到前一层,变成../file
    for file1 in os.listdir(dir+'/'+file):
      if(os.path.isdir(dir+'/'+file+'/'+file1)):
        Bring_All(dir+'/'+file+'/'+file1,dir+'/'+file)
  '''
  '''
  for file in os.listdir(dir):                              #将年份添加到所属文件夹名字并移出到上一层
    for file1 in os.listdir(dir+'/'+file):
      if(os.path.isdir(dir+'/'+file+'/'+file1)):
        os.renames(dir+'/'+file+'/'+file1,dir+'/'+file+'-'+file1)
        print(dir+'/'+file+'-'+file1)
  '''
  '''
                                                        #移动固定页数到固定文件夹
  sta=216
  #开始页数
  end=240
  #结束页数
  count=11
  #文件夹名字
  while(sta<end or sta==end):
    os.rename(dir+'/'+str(sta)+'.jpeg',dir+'/'+str(count)+'/'+str(sta)+'.jpeg')   #模式1
  
    if(sta<10):
      os.rename(dir+'/000'+str(sta)+'.jpg',dir+'/'+str(count)+'/000'+str(sta)+'.jpg') #模式2
    elif(sta<100 and sta>9):
      os.rename(dir+'/00'+str(sta)+'.jpg',dir+'/'+str(count)+'/00'+str(sta)+'.jpg')
    elif(sta<1000 and sta>99):
      os.rename(dir+'/0'+str(sta)+'.jpg',dir+'/'+str(count)+'/0'+str(sta)+'.jpg')

    sta=sta+1
  '''
  '''
  for file in os.listdir(dir):                              #根据文件里的特征创建文件夹，然后把对应特征的文件放进去
    if(os.path.isfile(dir+'/'+file)):
      rt=re.match(r'\d{5,15}',file)
      if(rt!=None):
        if(not os.path.exists(dir+'/'+str(rt.group()))):
          os.mkdir(dir+'/'+str(rt.group()))
        os.rename(dir+'/'+file,dir+'/'+str(rt.group())+'/'+file)
        print(dir+'/'+str(rt.group())+'/'+file)
  '''
  '''                                                     #给新建文件夹改名
  for file in os.listdir(dir):
    if(re.match('新建',file)):
      for file1 in os.listdir(dir+'/'+file):
        rt=re.search(r'[】](.*?)[#]',file1)
        if(rt!=None):
          #print(rt.group())
          name1=rt.group()[1:-1]
          print(name1)
          if(os.path.exists(dir+'/'+file)):
            os.renames(dir+'/'+file,dir+'/'+name1)
        print(file1)
  '''

  '''
  for file in os.listdir(dir):                          #检测空文件夹，暂时没法删除
    if(os.path.isdir(dir+'/'+file)): 
      if(not os.listdir(dir+'/'+file)):
        #os.remove(dir+'/'+file)
        print(dir+'/'+file)
    else:
      print('文件:'+file)
  '''
'''
for file in os.listdir(dir):                        #统一修改文件后缀名
    if(re.search('iso',file)):
      os.rename(dir+'/'+file,dir+'/'+file[:-3]+'rar')
'''
'''
def phash(img_addr):
    #第一步,处理图片为32x32，并转为灰度图，数字也用浮点数表示
    img=cv2.imread(img_addr)
    img=cv2.resize(img,(32,32))
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=img.astype(np.float32)

    #第二步，离散余弦变化
    img=cv2.dct(img)
    img=img[0:8,0:8]
    sum=0.
    hash_str=''

    #第三步,计算均值
    #avg=np.sum（img)/64.0
    for i in range(8):
        for j in range(8):
            sum+=img[i,j]
    avg=sum/64.0                                                

    #第四部,获得哈希
    for i in range(8):
        for j in range(8):
            if(img[i,j]>avg):
                hash_str=hash_str+'1'
            else:                                               #一共64位哈希值
                hash_str=hash_str+'0'
    return hash_str


def Haming_Distance(hash1,hash2):                                 #汉明距离不同有15，以下判定为相似以上则判断为不同
    num=0
    if(len(hash1)==len(hash2)):
        for i in range(len(hash1)):
            if(hash1[i]!=hash2[i]):
                num+=1
        return num
    else:
        print("Amount of Hash Code different")
        return -1

'''
@metric
def InterComparsion(dir):
  Hash_List=[]
  name_List=[]
  for file in os.listdir(dir):
    if(os.path.isfile(dir+'/'+file)):
      Hash_List.append(phash(dir+'/'+file))
      name_List.append(file)
  print('Inter done')
  return Hash_List,name_List

@metric
def Bring_All(dir,save_path):                         #将各个小文件夹全部取出放到存储路径
    for file in os.listdir(dir):
      if(os.path.isdir(dir+'/'+file)):
        dir1=dir+'/'+file
        Bring_All(dir1,save_path)
      else:
        if(not os.path.exists(save_path+'/'+file)):
          os.rename(dir+'/'+file,save_path+'/'+file)
        else:
          print(save_path+'/'+file[:-4]+'-1'+file[-4:])
          os.rename(dir+'/'+file,save_path+'/'+file[:-4]+'-1'+file[-4:]) #这样不好，弄不成一个系列，但可以用
        
      if(re.search(r'[[](.*?)[]]',file)):            #获取方括号里的东西
        ret=re.search(r'[[](.*?)[]]',file)
        print(ret.span())                             #xxx.span()返回元组,获得其中的数字用min(),max()
        fir=min(ret.span())           
        las=max(ret.span())
        print(file[:fir]+file[las:]) 
        os.rename(dir+'/'+file,dir+'/'+file[:fir]+file[las:])         


@metric
def Keep_Name(dir,save_path):                         #保存小文件夹名字到下一层的文件然后取出到存储路径
    for file in os.listdir(dir):
      if(os.path.isdir(dir+'/'+file)):
        dir1=dir+'/'+file
        Keep_Name(dir1,save_path)
      else:
        rt=re.search('】/',dir+'/'+file)              #需要提供一个特征来捕捉目标文件夹，比如】/1，1文件夹中为想要提取出来的文件,则填】
        print(rt.span())
        las=max(rt.span())
        print((dir+'/'+file)[las:])
        name=re.sub('/','-',(dir+'/'+file)[las:])
        os.rename(dir+'/'+file,save_path+'/'+name)

def main():
  if(flag==1):
    test(dir,save_path)
  elif(flag==2):
    Bring_All(dir,save_path)
  elif(flag==3):
    Keep_Name(dir,save_path)
  elif(flag==4):
    Hash_List,name_List= InterComparsion(dir)
    
    for i in range(len(Hash_List)):
      rewrite_List=[]
      count=1
      count1=1
      for j in range(i,len(Hash_List)):
        Ham_Dis=Haming_Distance(Hash_List[i],Hash_List[j])
        if(Ham_Dis<5 and Ham_Dis>0):
          print("%s and %s Haming_Distance is %d" % (name_List[i],name_List[j],Ham_Dis))
        '''
        if(Ham_Dis<5 and Ham_Dis>0):                                                              #汉明距离参数需定义，多少才为相似
          while(os.path.exists(dir+'/'+name_List[i][:-4]+'-'+str(count1)+name_List[i][-4:])):
            count1=count1+1
          if(os.path.exists(dir+'/'+name_List[i][:-4]+'-'+str(count1)+name_List[i][-4:])):  
            os.rename(dir+'/'+name_List[j],dir+'/'+name_List[i][:-4]+'-'+str(count1)+name_List[i][-4:])
          count1=1
        '''
  elif(flag==5):
    count2=1
    for file in os.listdir(dir):
      os.rename(dir+'/'+file,dir+'/'+str(count2)+file[-4:])
      count2=count2+1
        
        
    

if __name__=='__main__':
    main()
    print('done')