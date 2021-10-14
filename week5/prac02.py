#태어난 연도 입력->정수
#나이계산
#조건맞춰 결과 생성
#결과 추가
import datetime

cur_year = datetime.datetime.today().year
print(cur_year)
year = int(input("태어난 연도:"))
age = cur_year - year + 1

if 26>= age and age >=20:
    grade = "대학생"
elif 20 > age >=17:
    grade = "고등학생"
elif 17 > age >=14:
    grade ="중학생"
elif 14> age >=8:
    grade ="초등학생"
else:
    grade = "학생이 아닙니다."

print(f"결과:{grade}")
