import os
from score import Score

path_name = "c:/s202144057"
full_filename = path_name + "/list.txt"

scores =[]

if not os.path.isdir(path_name):
    os.mkdir(path_name)
    
elif os.path.isfile(full_filename):
    f = open(full_filename, 'r')
    while True:
        line = f.readline().strip()
        if not line:
            break

        datas = line.split(',')
        if len(datas) == 4:
            n = datas[0]
            k = int(datas[1])
            e = int(datas[2])
            m = int(datas[3])
            s = Score(n, k, e, m)
            scores.append(s)
    f.close
    f=open(full_filename,'a')
    print(f"기존 등록되어 있는 학생은 {len(scores)}명입니다.")
elif not os.path.isfile(full_filename):
    f = open(full_filename,'w')
    
while True:
    print("1. 입력")
    print("2. 검색하기")
    print("3. 전체출력하기")
    print("4. 파일에서 다시 읽어오기")
    print("0. 종료")
    
    menu = input(">").strip()
    
    if menu =="1":
        name=input("이름을넣어주세요.(종료시:바로엔터) :").strip()
        if not name:
            break
        kor=input("국어 점수:")
        eng=input("영어 점수:")
        mat=input("수학 점수:")
    
        data=f"{name},{kor},{eng},{mat}\n"
        data = Score(name,int(kor),int(eng),int(mat))
        scores.append(data)
        f.write(data.file_content())

    elif menu =="2":
        print("원하는 이름으로 검색하세요. (빈 칸이면 종료)")
        findwhat = input("이름:").strip()
        if not findwhat:
            break
        # find = (item for item in scores if item[name]==findwhat)
        # if find:
        #     print(find.__str__)
        # elif not find:
        #     print(f"{findwhat}의 정보가 없습니다.")
        
        
        
        for score in scores:
            if score.name == findwhat:
                print(f"{score}")
                break
            #못찾았을때 출력문...
            
            
                
    elif menu == "3":
        print(f"기존 등록되어 있는 학생 {len(scores)}명의 정보입니다.")
        for score in scores:
            print(score)
        
    elif menu == "4":
        print("미구현 기능입니다.")
    elif menu =="0":
        break