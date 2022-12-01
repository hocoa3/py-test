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
    def __init__(self):
        self.file=r'C:\Users\86178\Desktop\BOM_Template1.xlsx'
        self._wb=openpyxl.load_workbook(self.file)
        self._ws=self._wb.active

    def Write_OnebyColumn_mark(self,list):
        component_pos='C8'
        pos=component_pos
        for x in range(len(list)):
            self.Write_One_Block(pos,list[x])
            pos=pos[0]+str(x+8+1)
        self.Save()

    def Write_OnebyColumn_Quantity(self,list):
        component_pos='G8'
        pos=component_pos
        for x in range(len(list)):
            self.Write_One_Block(pos,list[x])
            pos=pos[0]+str(x+8+1)
        self.Save()

    def Write_OnebyColumn_number(self,list):
        component_pos='B4'
        pos=component_pos
        for x in range(1,len(list)+4):
            self.Write_One_Block(pos,x)
            pos=pos[0]+str(x+4+1)
        self.Save()
    
    def Write_OnebyColumn_unit(self,list):
        component_pos='F8'
        pos=component_pos
        for x in range(1,len(list)):
            self.Write_One_Block(pos,'个')
            pos=pos[0]+str(x+8+1)
        self.Save()

    def Write_OnebyColumn_VolumeandFootPrint(self,list_V,list_F):
        component_pos='E8'
        pos=component_pos
        for x in range(len(list_V)):
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
            pos=pos[0]+str(x+8+1)
        self.Save()
    
    

    def Save(self):
        self._wb.save(self.file)
        print('save done')

if __name__=='__main__':
    name1='BOM_Test.xlsx'                                                   #物料清单源文件名字在此输入
    BOM1=BOM_List(name1)
    #dat=BOM1.Read_One_Block('C8')
    mark_list=BOM1.Read_One_Column(4)
    volume_list=BOM1.Read_One_Column(1)
    footprint_list=BOM1.Read_One_Column(2)
    quantity_list=BOM1.Read_One_Column(3)
    Template=Template_List()

    Template.Write_OnebyColumn_mark(mark_list)
    Template.Write_OnebyColumn_VolumeandFootPrint(volume_list,footprint_list)
    Template.Write_OnebyColumn_Quantity(quantity_list)
    Template.Write_OnebyColumn_number(mark_list)
    Template.Write_OnebyColumn_unit(mark_list)
    print('done')

    
    
