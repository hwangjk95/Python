import os
from score import Score

def inputmenu():
    print("1. 입력")
    print("2. 검색")
    print("3. 전체조회")
    print("0. 종료")
    return input(">").strip()

def view():
    for score in scores:
        print(score)
    print(f"총 인원수:{len(scores)}")

def search():
    while True:
        name = input("이름:").strip()
        if not name:
            break
        searchscore = None
        for score in scores:
            if score.name == name:
                searchscore = score
                print(score)
                break
        if not searchscore:
            print("일치하는 정보가 없습니다.") 
        #연습: 동명이인 해결해보기

def register():
    while True:
        name = input("이름: ").strip()
        if not name:
            break
        try:
            kor = int(input("국어:"))
            eng = int(input("영어:"))
            mat = int(input("수학:"))
        except:#정수를 잘못입력했을때
            continue
        score = Score(name, kor, eng, mat)
        scores.append(score)

        # f=open(filename,'a')
        # f.write(score.file_content())
        # f.close()

        with open(fullname, 'a')as f:
            f.write(score.file_content())

def startinfo():
    if not os.path.isdir(pathname):
        os.mkdir(pathname)
    elif os.path.isfile(fullname):
        with open(fullname,'r') as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break
                data = line.split(',')
                if len(data)==4:
                    name = data[0]
                    kor = int(data[1])
                    eng = int(data[2])
                    mat = int(data[3])

                    scores.append(Score(name, kor, eng, mat))
        print("기존 인원:",len(scores))
pathname = "c:/week12"
filename = "data.csv" #csv는 ,같은걸로 데이터를 구분하는? 파일
fullname = pathname + "/" + filename

scores = []
#사전작업 끝

#프로그램 시작하자마자 체크
startinfo()

#메뉴를 반복적으로 보여주면서 해당 내용을 계속 실행
while True:
    menu = inputmenu()
    if menu =="1":
        register()
    elif menu =="2":
        search()
    elif menu =="3":
        view()
    elif menu == "0":
        break
