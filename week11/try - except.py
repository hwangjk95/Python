#try-except.py
file = "c:/abc/abc.txt"
try:
    f = open(file,'r')
    f.close()
except:
    print("파일이 없어:"+file)
while True:
    try:
        mod = int(input("숫자:"))
        a = 10/ mod    
        kor = int("백")
    except ZeroDivisionError:
        print("0넣지마!")
    except ValueError:
        print("정수형 문자열을 넣으세요.")
    except: #에러가 생겼다고 프로그램이 끝나지 않음
        print("응?")
        