import re
import os 
import os.path


dir='C:/Users/86178/BaiduNetDisk'
save_path='D:/GreemBang作品合集/GreemBang/[Patreon] Greem Bang -2021年2月'

def test():
  for file in os.listdir(dir):                        #统一修改文件后缀名
    if(re.search('iso',file)):
      os.rename(dir+'/'+file,dir+'/'+file[:-3]+'rar')
   
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