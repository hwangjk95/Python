class Contact:
    def __init__(self, name, phone="", addr=""):
        self.name = name
        self.phone = phone
        self.address = addr
    def __str__(self):
        return f"{self.name} | {self.phone} | {self.address}"

contact_list = list()
# contact1 =Contact("김미영", "000-0000-0000", "인천광역시 연수구")
# contact2 = Contact("김미자")
# contact3 = Contact(name="이미영", addr="경기도 부천시")#contact4 = Contact()
contact_list.append(Contact("김미영", "000-0000-0000", "인천광역시 연수구"))
contact_list.append(Contact("김미자"))
contact_list.append(Contact(name="이미영", addr="경기도 부천시"))

for c in contact_list:
    print(c)#print(f"{self.name} | {self.phone} | {self.address}")

