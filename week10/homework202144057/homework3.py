import os
import score

path_name = "c:/202144057" #본인학번
full_filename = path_name + "/list.txt"

if not os.path.isfile(full_filename):
    print("파일이 존재하지 않습니다.")
else:
    f = open(full_filename, 'r')

    scores = []
    while True:
        line = f.readline().strip()
        if not line:
            break

        datas = line.split(',')
        if len(datas) == 4:
            n = datas[0]
            k = int(datas[1])
            e = int(datas[2])
            m = int(datas[3])
            s = score.Score(n, k, e, m)
            scores.append(s)
    f.close()
    for s in scores:
        print(s)