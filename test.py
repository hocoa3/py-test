import re
import os 
import os.path


dir='D:/osisio(CG,棒)'
save_path='D:/Nahaki(插画,很棒，等待更新)#21.10'
flag=1
#flag=1时为test,2为Bring_all,3为Keep_name
def test():
  for file in os.listdir(dir):                              #将年份添加到所属文件夹名字并移出到上一层
    for file1 in os.listdir(dir+'/'+file):
      if(os.path.isdir(dir+'/'+file+'/'+file1)):
        os.renames(dir+'/'+file+'/'+file1,dir+'/'+file+'-'+file1)
        print(dir+'/'+file+'-'+file1)
  '''                                                       #移动固定页数到固定文件夹
  sta=362                     #开始页数
  end=384                     #结束页数
  count=20                    #文件夹名字
  while(sta<end or sta==end):
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
  '''                            #给新建文件夹改名
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
        os.remove(dir+'/'+file)
        print(dir+'/'+file)
    else:
      print('文件:'+file)'''
  '''for file in os.listdir(dir):                        #统一修改文件后缀名
    if(re.search('iso',file)):
      os.rename(dir+'/'+file,dir+'/'+file[:-3]+'rar')'''
   
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
        
'''      if(re.search(r'[[](.*?)[]]',file)):            #获取方括号里的东西
        ret=re.search(r'[[](.*?)[]]',file)
        print(ret.span())                             #xxx.span()返回元组,获得其中的数字用min(),max()
        fir=min(ret.span())           
        las=max(ret.span())
        print(file[:fir]+file[las:]) 
        os.rename(dir+'/'+file,dir+'/'+file[:fir]+file[las:])         '''


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
    test()
  elif(flag==2):
    Bring_All(dir,save_path)
  elif(flag==3):
    Keep_Name(dir,save_path)

if __name__=='__main__':
    main()
    print('done')