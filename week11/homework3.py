import os
from score import Score

path_name = "c:/202144057"
full_filename = path_name + "/list.txt"

if os.path.isfile(full_filename):
    f=open(full_filename,'w')
    
    
    
    
    
    
    datas=line.split(',')
    if len(datas) ==4:
        try:
            s =score.Score(datas[0],int(datas[1]),int(datas[2]),int(datas[3]))
            scores.append(s)
        except:
            print("분석오류:",line)
            continue
        
f.close()

for s in scores:
    print(s)