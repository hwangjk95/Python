import os


path_name = "c:/202144057"
full_filename = path_name + "/list.txt" #저장할 파일의 전체경로

if not os.path.isdir(path_name):
    os.makedirs(path_name)
    
    
f=open(full_filename,'a')
while True:
    name=input("이름을넣어주세요.(종료시:바로엔터) :").strip()
    if not name:
        break
    kor=input("국어 점수:")
    eng=input("영어 점수:")
    mat=input("수학 점수:")
    
    data=f"{name},{kor},{eng},{mat}\n"
    f.write(data)
    
f.close