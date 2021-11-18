number = input("4자리의 정수 입력:")#number = "1234"

#number_int = [int(n) for n in number]#[1, 2, 3, 4]
#리스트(0~n-1), 문자열(0~n-1)

number_int = list(map(int, number)) #개별요소를 int형으로 형변환

print(sum(number_int))

