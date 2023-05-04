# 개인정보 수집 유효기간
def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split('.')))
    
    term = {}
    for s in terms:
        sp = s.split(' ')
        term[sp[0]] = int(sp[1])
    
    for i in range(len(privacies)):
        p = privacies[i].split(' ')
        date = list(map(int, p[0].split('.')))
        date[1] += term[p[1]]
        while date[1] > 12:
            date[1] -= 12
            date[0] += 1
        if date[0] < today[0]:
            answer.append(i+1)
        elif date[0] == today[0]:
            if date[1] < today[1]:
                answer.append(i+1)
            elif date[1] == today[1]:
                if date[2] <= today[2]:
                    answer.append(i+1)
    return answer

# 찾아낸 코드
from datetime import datetime, timedelta

def solution(today, terms, privacies):
    answer = []
    today = datetime.strptime(today, '%Y.%m.%d')
    
    term = {k: int(v) for k, v in [s.split(' ') for s in terms]}
    
    for i in range(len(privacies)):
        p = privacies[i].split(' ')
        date = datetime.strptime(p[0], '%Y.%m.%d')
        delta = timedelta(months=term[p[1]])
        due_date = date + delta
        
        if due_date < today:
            answer.append(i+1)
    return answer


a = solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
print(a)