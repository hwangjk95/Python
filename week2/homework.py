full=input("주민등록번호(예제:001212-3456789):")

front=full[0:6]
rear=full[7:]

birth=f"연월일:{front}"
s=f"성별:{rear[0]}"
print(birth)
print(s)
