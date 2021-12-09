f1 =open("c:today/data.csv",'r')
f2 = open("c:today/data.ini",'w')

while True:
    data = f1.readline().strip()
    if not data:
        break
    datas = data.split(',')
    if len(datas) == 5:
        f2.write(f"[CODE_{datas[0]}]\n")
        f2.write(f"DESC={datas[1]}\n")
        f2.write(f"STT={datas[2]}\n")
        f2.write(f"LOSSCODE={datas[3]}\n")
        f2.write(f"LOSSDESC={datas[4]}\n\n")

f1.close()
f2.close()