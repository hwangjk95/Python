car = 'KIA'
print(car=='Kia')
print(car.lower() == 'kia')
print(car.lower() != 'bmw')
print('*' * 30)

myage = 22
yourage = 19
print(myage >= 21 and yourage >= 21)
print(myage >= 21 or yourage >= 21)
print('*' * 30)

cars = ['audi', 'tesla', 'benz', 'kia', 'lincoln', 'hyundai']
print(car in cars)
print(car not in cars)
print(car.lower()  in cars)
print(car.lower() not in cars)
print('*' *30)

t1=True
t2=False
t3=3<=2
t4 = 5!=3
year = 2021
t5 = ((year % 4 ==0) and (year % 100 !=0)) or (year %400 ==0)
print(t1, t2, t3, t4, t5)
