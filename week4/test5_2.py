#김인하씨의 과목별 점수를 가지고 평균을 구해보자.
#리스트 사용
#for 사용
lect =('국어','영어','수학','과학')
scores = []
for l in lect:
    scores.append(int(input(f"{l} 점수:")))
avg = sum(scores)/len(scores)

print(f"{'과목':^4} {'점수':^4}")
print("="*12)

#for i in range(len(lect)):
 #   print(f"{lect[i]:^4}{scores[i]:>4}")

for i, lec in enumerate(lect) :
    print(f"{lect[i]:^4}{scores[i]:>4}")

print(f"\n평균:{avg:0.2f}")