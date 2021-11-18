print("놀이동산 입장권")
age = int(input("나이:"))
tp = int(input("주간입장권 (1), 야간입장권(2):"))

price = 0
#1번 - 8세 이상이면 4000원, 나미저니느 0원
if age >= 8 :
    price = 4000
print(f"#1번 가격:{price}원 입니다.", end="\n\n")

#2번 - 8세 이상이면 4000원(성인요금), 나머지는 0원 (영유아요금)
if age >= 8 :
    adult = "성인"
    price = 4000
else :
    adult = "영유아"
    price= 0

print(f"#2번 {adult}요금-{price}원 입니다.",end="\n\n")

#3 - 19세 이상이면 4000원(성인), 8~18,70세 이상이면 3000원(특별요금),영유아요금 0
if age<8:
    adult = "영유아"
    price = 0
elif age<=18 :
    adult = "특별"
    price = 3000
elif age <70:
    adult = "성인"
    price = 4000
else:
    adult = "특별"
    price = 3000
print(f"#3번 {adult}요금-{price}원 입니다.",end="\n\n")

#4 - 19세 이상이면 4000원(성인), 8~18,70세 이상이면 3000원(특별요금),영유아요금 0
if age<8:
    adult = "영유아"
    price = 0
elif age<=18 or age>= 70:
    adult = "특별"
    price = 3000
else:
    adult = "성인"
    price = 4000
print(f"#4번 {adult}요금-{price}원 입니다.",end="\n\n")

#5 - 19세 이상이면 4000원(성인), 8~18,70세 이상이면 3000원(특별요금),영유아요금 0
#단, 야간의 경우 나이와 상관없이 모두 2000원
if age<8:
    adult = "영유아"
    price = 0
elif tp ==1:
    if age <= 18 or age >= 70:
        adult = "특별"
        price = 3000
    else:
        adult = "성인"
        price = 4000
else:
    adult = "야간"
    price = 2000

print(f"#5번 {adult}요금-{price}원 입니다.",end="\n\n")