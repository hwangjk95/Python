def test(a, b, c=20, d=20):
    print(a, b, c, d)

def entrance(name, grade=1):
    print("입학을 축하합니다")
    print(f"이름:{name}")
    print(f"학년:{grade}")

entrance("김인하")
entrance("이인하")
entrance("박인하")
entrance("최인하")
entrance("신인하",2) 


#test()
test(1,2,3,4)
test(b=2,c=3,a=1,d=4)
test(1,2)