# 햄버거 만들기
def solution(ingredient):
    answer = 0   
    
    ing = list()
    
    for i in ingredient:
        ing.append(i)
        if ing[-4:] == [1,2,3,1]:
            del ing[-4:]
            answer += 1
    
    return answer


# 2022 카카오 성격유형 검사
def solution(survey, choices):
    answer = ''

    socres = {
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0
    }

    for i in range(len(survey)):
        if choices[i] > 4:
            socres[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            socres[survey[i][0]] += 4 - choices[i]

    socres = list(socres.items())
    for i in range(0, len(socres), 2):
        if socres[i][1] < socres[i+1][1]:
            answer += socres[i+1][0]
        else :
            answer += socres[i][0]


    return answer

# 풀이 못함
def solution(players, callings):
    for calling in callings:
        idxing = players.index(calling)
        players[idxing-1], players[idxing] = players[idxing], players[idxing-1]

    return players

a = solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"])
print(a)
