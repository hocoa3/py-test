import os
import re

if __name__=='__main__':
    #path=os.getcwd()
    path='C:/Users/86178/BaiduNetDisk'
    for file in os.listdir(path):
        if(os.path.isfile(path+'/'+file)):
            if(not re.search('[.]',file)):
                os.rename(path+'/'+file,path+'/'+file+'.rar')
            else:
                idx=file.index('.')
                if(re.search('7',file[idx:]) or re.search('z',file[idx:])):
                    os.rename(path+'/'+file,path+'/'+file[:idx]+'.7z')
                elif(re.search('r',file[idx:]) or re.search('a',file[idx:])):
                    os.rename(path+'/'+file,path+'/'+file[:idx]+'.rar')
                elif(re.search('z',file[idx:]) or re.search('i',file[idx:])or re.search('p',file[idx:])):
                    os.rename(path+'/'+file,path+'/'+file[:idx]+'.zip')

