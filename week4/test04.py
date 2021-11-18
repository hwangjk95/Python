#4자리의 정수를 받는다.
#문자열 ->정수

#4번,3번,2번,1번 각 자리별 숫자를 뽑는다.
#//,%
#각 자리의 수의 합을 계싼하고
#출력한다.

numbers = int(input("4자리의 정수 입력:"))
#"1234" =>1234
# 1+ 2+ 3+ 4=10
result = 0
for i in [1000, 100, 10, 1]:
    result += numbers // i
    numbers %= i

#n4 = numbers // 1000  #1234//1000 = 1
#numbers = numbers %1000 # 1234%1000=2341

#n3 = numbers // 100
#numbers = numbers %100

#n2 = numbers // 10
#numbers = numbers %10

#n1 = numbers // 1
#numbers = numbers % 1

#result = n4+n3+n2+n1

print(result)
