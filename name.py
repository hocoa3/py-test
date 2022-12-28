import openpyxl
import re

dir=r'G:'
name=r'副本-无尽战区重启签名活动——重启 ！让野火不熄.xlsx'
dir=dir.replace('\\','/')   
wb=openpyxl.load_workbook(dir+'/'+name)

print(wb.sheetnames)

mode=re.compile(r'(ID|id)\s*?(:|：| )')
mode2=re.compile(r'.+(:|：)')
mode3=re.compile(r'(ID|id)\s*?')
ws=wb['签名楼+留言墙+回忆区-展示页']
for cell in ws['B33':'C62']:
    for each in cell:
        #print(each.value)
        if(mode.match(str(each.value)) != None):
            print('1 '+each.value)
        elif(mode2.match(str(each.value)) != None):
            print('2 '+each.value)
        elif(mode3.match(str(each.value)) != None):
            print('3 '+each.value)
#wb.save(dir+'/'+name)







print('done')





