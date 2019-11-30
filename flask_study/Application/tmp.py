import re
import time

with open('data.txt','r') as f:
    lists = f.readlines()
    for text in lists:
        name_e = re.findall('（(.*?)）',text)
        if name_e == []:
            name_e = ''
        else:
            name_e = name_e[0]
        name = text.split('（')
        name = name[0].replace('\n','')
        print(name)
        print(name_e)
        print('-----------------------')
        with open('data_new11.csv','a') as w:
            w.write(name+','+name_e+'\n')
