list = []
sum =0
for i in range(0,5):
    name=input("이름을 입력해주세요:")
    score=int(input("점수를 입력해주세요:"))
    sum += score
    list.append({'name':name,'score':score})


print(f"전체 평균:{sum/5}")
