list={}

while True:   
    name=input("이름:")
    if name == '':
        break;   
    number=input("연락처:")
    
    list[name] = number


print("=====연락처목록=====")
for name, number in list.items():
    print(f"{name}:{number}")
