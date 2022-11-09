import re
import os 
import os.path


dir='D:/まりさやか/近期作品'
save_path='D:/GreemBang作品合集/GreemBang/[Patreon] Greem Bang -2021年2月'

def test():
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
        rt=re.search('月/',dir+'/'+file)
        print(rt.span())
        las=max(rt.span())
        print((dir+'/'+file)[las:])
        name=re.sub('/','-',(dir+'/'+file)[las:])
        os.rename(dir+'/'+file,save_path+'/'+name)

def main():
  test()
  #Bring_All(dir,save_path)
  #Keep_Name(dir,save_path)

if __name__=='__main__':
    main()
    print('done')