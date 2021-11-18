import os
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
            score = {}
            score['name'] = datas[0]
            score['kor'] = int(datas[1])
            score['eng'] = int(datas[2])
            score['mat'] = int(datas[3])
            scores.append(score)
    f.close()

    for s in scores:
        line = f"이름:{s['name']} 국어:{s['kor']} 영어:{s['eng']} 수학:{s['mat']}"
        avg = sum([s['kor'], s['eng'], s['eng']]) / 3
        line += f" 평균={avg:0.2f}"
        print(line)