import datetime

cur_year = datetime.datetime.today().year
datetime.datetime.today().month
datetime.datetime.today().day

socnum = input("주민등록번호:")
y = int(socnum[:2])
g = int(socnum[7])

if g <=2:
    y += 1900
else:
    y += 2000

age = cur_year - y + 1
print("너의 나이는 ...",age)