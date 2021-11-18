#선택한 도형의 넓이를 계산하는 프로그램을 작성하세요.
#도형의 종류는 사각형, 삼각형, 원으로 하고, 도형의 종류에 따라 입력값을 다르게 해서 계산에 사용합니다.
#소숫점 두자리수까지 표현

type = int(input("도형 선택(1:사각, 2:삼각, 3:원):"))

if type==1 :
    x=int(input("가로 입력:"))
    y=int(input("세로 입력:"))
    c=x * y
    print(f"도형의 넓이 = {c:0.2f}")
elif type==2 :
    x=int(input("밑변 입력:"))
    y=int(input("높이 입력:"))
    c=1/2*x*y
    print(f"도형의 넓이 = {c:0.2f}")
elif type==3 :
    x=int(input("반지름 입력:"))
    c=3.14*x**2
    print(f"도형의 넓이 = {c:0.2f}")
else :
    print("잘못된 입력입니다.")
