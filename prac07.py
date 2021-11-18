contacts = {}

def search(name):
    #phone = contacts[name] #비추천 키가 없으면 죽음. 중간고사 이후에 상세설명
    phone = contacts.get(name)
    return phone

def addition():
    while True:
        name = input("이름:").strip()
        if not name:
            break

        if contacts.get(name):
            continue

        phone  = input("연락처:")
        contacts[name] = phone

    print("연락처목록=====")
    for key, value in contacts.items():
        print(f"{key} : {value}")

#실습 08
while True:
    print("="*20)
    print("[1] 추가")
    print("[2] 검색")
    print("[0] 종료")
    print("="*20)

    sel_menu = input("선택:").strip()

    if sel_menu == "1":
        addition()
    elif sel_menu == "2":
        #연습용 코드
        name = input("이름:").strip()
        phone = search(name)
        if phone:
            print(phone)
        else:
            print("없다")
    elif sel_menu == "0":
        break
