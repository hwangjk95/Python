import csv
header = []
incheondata = []
with open("./korea_floating_population_data.csv",'r', encoding="cp949") as f1:
    reader = csv.reader(f1)
    for index, row in enumerate(reader): #enumerate > 두개 동시에 뽑아줌
        if index == 0:                      #쉽표 기준으로 나눠서 리스트로 만들어줌.. 행으로 쪼개고 열단위로 쪼개고
            header = row
        else:
            if row[7].find("인천광역시") != -1:
                incheondata.append(row)

with open("./incheon_floating_population_data.csv",'w',encoding="utf8",newline="") as f2: #newline >> 빈줄 제거
    wr = csv.writer(f2, delimiter="\t")#delimiter 는 구분자 설정
    wr.writerow(header)
    wr.writerows(incheondata)
    
    
#성별 기준으로 쪼개서 다시 구성해보기
#ex 남자60대가 선호하는 구역