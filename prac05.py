scores = [
    [49,80,20,100,80],
    [43,60,85,30,90],   #None , -1 생각해보기
    [49,82,48,50,100]
    ]

#sum_scores = [0,0,0,0,0]
sum_scores = [0 for i in scores[0]]

for subject in scores:
    #i = 0
    for i, score in enumerate(subject):  #튜플형태?
        sum_scores[i] += score
        #i+=1

'''avg_scores = []
for score in sum_scores:
    avg_scores.append(score/ len(scores))'''

avg_scores = [ score / len(scores)for score in sum_scores]

print(avg_scores)

#시험문제 출제