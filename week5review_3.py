students = {}
number =int(input("학생수:"))

sum = 0
for i in range(1,number+1):
    name =input("이름:")
    score = float(input("성적:"))
    students[name] = score
    sum += score

print(students)
avg = sum /number
avg = sum(students.values()) / number
print(avg)