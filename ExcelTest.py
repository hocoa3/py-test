import openpyxl
from enum import Enum
import re

#dir2=r'C:\Users\86178\Desktop\'


#dir2=dir2.replace('\\','/')

class Alphabet(Enum):
    A=1
    B=2
    C=3
    D=4
    E=5
    F=6
    G=7
    H=8
    I=9
    J=10
    K=11
    L=12
    M=13
    N=14
    O=15
    P=16
    Q=17
    R=18
    S=19
    T=20
    U=21
    V=22
    W=23
    X=24
    Y=25
    Z=26

class Component():
    def __init__(self,mark,footprint,volume,num,quantity):
        self.mark=mark
        self.footprint=footprint
        self.volume=volume
        self.num=num
        self.quantity=quantity

class BOM_List():
    def __init__(self,filename):
        dir=r'C:\Users\86178\Desktop'
        self.dir=dir.replace('\\','/')
        self.filename=filename
        self._wb=openpyxl.load_workbook(self.dir+'/'+self.filename)
        self._ws=self._wb.active

    def Read_One_Block(self,loc):
        print(self._ws[loc].value)
        return self._ws[loc].value

    def Read_One_Row(self,row):
        List=[]
        for col in range(1,self._ws.max_column+1):
            loc=str(Alphabet(col))[-1]+str(row)
            if(self._ws[loc].value != None):
                print(self._ws[loc].value)
                List.append(self._ws[loc].value)
        return List

    def Read_One_Column(self,col,sta_row=6):
        List=[]
        for row in range(sta_row,self._ws.max_row+1):
            loc=str(Alphabet(col))[-1]+str(row)
            if(self._ws[loc].value != None):
                #print(self._ws[loc].value)
                List.append(self._ws[loc].value)
        return List

    def Write_One_Block(self,pos,data):
        self._ws[pos]=data
        print("%s has rewrited to %s"%(pos,data))
        
   
    def Save(self):
        self._wb.save(self.dir+'/'+self.filename)
        print('save done')

class Template_List(BOM_List):
    def __init__(self,name):
        self.file=r'C:\Users\86178\Desktop'
        self.file=self.file.replace('\\','/')
        self.file=self.file+'/'+name
        self._wb=openpyxl.load_workbook(self.file)
        self._ws=self._wb.active

    def Write_OnebyColumn_mark(self,list):
        component_pos='C8'
        pos=component_pos
        off=0
        for x in range(len(list)):
            num=len(list[x].split(', '))
            if(num>=4):
                name=list[x].split(', ')
                
                while(num>4):
                    dat=name[0]+', '+name[1]+', '+name[2]+', '+name[3]+', '
                    self.Write_One_Block(pos,dat)
                    off=off+1
                    pos=pos[0]+str(x+8+off)
                    num-=4
                    name=name[4:]
                if(len(name)==1):
                    dat=name[0]
                else:
                    dat=''
                    for x in range(len(name)):
                        dat=dat+name[x]+', '
                    dat=dat[:-2]
                self.Write_One_Block(pos,dat)
                print('pos1%s'% pos)
            else:
                pos=pos[0]+str(x+8+off)
                self.Write_One_Block(pos,list[x])
                print('pos2%s'% pos)
            pos=pos[0]+str(x+8+1+off)
        print(pos)
        self.Save()

    def Write_OnebyColumn_Quantity(self,list):
        component_pos='G8'
        pos=component_pos
        off=0
        for x in range(len(list)):
            num=list[x]
            self.Write_One_Block(pos,list[x])
            while(num>4):
                pos=pos[0]+str(x+8+1+off)
                off+=1
                self.Write_One_Block(pos,None)
                num-=4
            pos=pos[0]+str(x+8+1+off)
        self.Save()

    def Write_OnebyColumn_number(self,list,quantity):
        component_pos='B4'
        pos=component_pos
        off=0
        idx=0
        num=0
        for x in range(1,len(list)+5):
            if(x>4):
                num=quantity[idx]
            self.Write_One_Block(pos,x)
            while(num>4):
                pos=pos[0]+str(x+4+off)
                off+=1
                self.Write_One_Block(pos,None)
                num-=4
            pos=pos[0]+str(x+4+off)
            if(x>4):
                idx+=1
            print(x)
        self.Save()
    
    def Write_OnebyColumn_unit(self,list,quantity):
        component_pos='F8'
        pos=component_pos
        off=0
        for x in range(0,len(list)):
            num=quantity[x]
            self.Write_One_Block(pos,'个')
            while(num>4):
                pos=pos[0]+str(x+8+1+off)
                off+=1
                self.Write_One_Block(pos,None)
                num-=4
            pos=pos[0]+str(x+8+1+off)
        self.Save()

    def Write_OnebyColumn_VolumeandFootPrint(self,list_V,list_F,quantity):
        component_pos='E8'
        pos=component_pos
        off=0
        for x in range(len(list_V)):
            num=quantity[x]
            if(re.search('F',str(list_V[x])) and re.match(r'\d{4}',str(list_F[x]))):
                name='贴片电容'+str(list_F[x])+'-'+str(list_V[x])
            elif(re.search('F',str(list_V[x])) and re.match(r'\d{3}',str(list_F[x]))):
                name='贴片电容0'+str(list_F[x])+'-'+str(list_V[x])
            elif(re.match(r'\d{3} \d{3} \d{3}',str(list_V[x]))):
                name='磁珠0'+str(list_F[x])+'-'+str(list_V[x])
            elif(re.match(r'\d{4}',str(list_F[x]))):
                name='贴片电阻'+str(list_F[x])+'-'+str(list_V[x])+'Ω'
            elif(re.match(r'\d{3}',str(list_F[x]))):
                name='贴片电阻0'+str(list_F[x])+'-'+str(list_V[x])+'Ω'
            else:
                name=str(list_V[x])  
            self.Write_One_Block(pos,name)
            while(num>4):
                pos=pos[0]+str(x+8+1+off)
                off+=1
                self.Write_One_Block(pos,None)
                num=num -4
            pos=pos[0]+str(x+8+1+off)
        self.Save()
    
    

    def Save(self):
        self._wb.save(self.file)
        print('save done')

if __name__=='__main__':
    name1='BOM_Test.xlsx'
    Template_name='BOM_Template1.xlsx'
    #物料清单源文件名字在此输入
    BOM1=BOM_List(name1)
    #dat=BOM1.Read_One_Block('C8')
    mark_list=BOM1.Read_One_Column(4)                                                         #读取下标
    volume_list=BOM1.Read_One_Column(1)                                                       #读取大小
    footprint_list=BOM1.Read_One_Column(2)                                                    #读取封装
    quantity_list=BOM1.Read_One_Column(3)                                                     #读取数量
    Template=Template_List(Template_name)

    Template.Write_OnebyColumn_mark(mark_list)                                                #处理下标
    Template.Write_OnebyColumn_VolumeandFootPrint(volume_list,footprint_list,quantity_list)   #处理封装和大小
    Template.Write_OnebyColumn_Quantity(quantity_list)                                        #处理数量
    Template.Write_OnebyColumn_number(mark_list,quantity_list)                                #处理序号
    Template.Write_OnebyColumn_unit(mark_list,quantity_list)                                  #处理单位
    
    print('done')

    
    
