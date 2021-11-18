#기호를 키보드를 통해 입력한다.
#기호 사이에 넣을 문자열을 키보드를 통해 입력 받는다.
#기호 사이에 문자열을 넣고, 화면에 출력한다.

symbols = input("기호:")
content = input("문자열:")
#기호[0] + 문자열 + 기호[-1]
result =symbols[0] + content + symbols[-1]
print(result)