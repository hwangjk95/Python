#1학기학점과 2학기학점의 평균을 구하고, 봉사시간이 8시간이상인지 참거짓을 구한다.
#if문을 사용하자.

First_half = float(input("1학기 학점:"))
Second_half = float(input("2학기 학점:"))
serve = int(input("봉사시간:"))
a=0
if (((First_half + Second_half)/2) >= 3.5) and serve >=8 :
    a= "True"
else :
    a="False"

print(f"장학금 대상 여부: {a}")
