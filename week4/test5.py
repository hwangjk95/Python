#김인하씨의 과목별 점수를 가지고 평균을 구해보자.
#변수 사용
kor=99
eng=88
mat=55
avg=(kor+eng+mat)/3

print(f"{'과목':^4} {'점수':^4}")
print("="*12)
print(f"{'국어':^4}{kor:>4}")
print(f"{'영어':^4}{eng:>4}")
print(f"{'수학':^4}{mat:>4}")
print(f"\n평균:{avg:0.2f}")