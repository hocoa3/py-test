import re
import os 
import os.path


dir='D:/GreemBang作品合集/GreemBang/[Patreon] Greem Bang -2021年2月'
save_path='D:/GreemBang作品合集/GreemBang/[Patreon] Greem Bang -2021年2月'

def test():
  year_a=2020
  year=2020
  month=12
  while(year>2019 and month>1):
    month_a=month-4
    if(month==1):
      month=12
      year=year-1
    elif(month_a<1):
      month_a=12
      year_a=year_a-1
    if(month<10):
      path=save_path+'/'+str(year)+'.0'+str(month)

    else:
      path=save_path+'/'+str(year)+'.'+str(month)

    if(month_a<10):
  
      path_a=save_path+'/'+str(year_a)+'.0'+str(month_a)
    else:

      path_a=save_path+'/'+str(year_a)+'.'+str(month_a)
    os.renames(path_a,path)
    month=month-1

   
def Bring_All(dir,save_path):
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


def Keep_Name(dir,save_path):
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
  #test()
  #Bring_All(dir,save_path)
  Keep_Name(dir,save_path)

if __name__=='__main__':
    main()
    print('done')