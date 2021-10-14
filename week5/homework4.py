#점수 입력받고 정수로 변환
# 90~A
#80~B
#70~C
#60~D
#F
score = int(input("점수:"))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >=70:
    grade = "C"
elif score >=60:
    grade = "D"
else:
    grade = "F"

if score >100 or score<0:
    print("입력 오류입니다.")
else:
    print(f"학점: {grade}")