#24조각을 5명이서 균등하게 나눳을때 몇조각이며, 남는것은 몇조각인지

people = int(input("명수:"))
pizza = int(input("피자주문수량:"))
piece = int(input("조각:"))

a = pizza * piece // people
b = pizza * piece % people

print(f"인당 {a}조각, 남은 조각{b}")