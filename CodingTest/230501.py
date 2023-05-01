# 숫자 짝꿍
def solution(X, Y):
    answer = ''
    
    XY_Set = set(X) & set(Y)
    for x in list(XY_Set):
        answer += x * min(X.count(x), Y.count(x))
    
    answer = ''.join(reversed(sorted(answer)))
    if answer == '':
        return '-1'
    elif answer.replace('0', '') == '':
        return '0'

    return answer


# 내가 한 코드 옹알이(2)
def solution(babbling):
    answer = 0
    baby_ask = ["aya", "ye", "woo", "ma"]
    
    
    for babl in babbling:
        for i in range(len(baby_ask)):
            if baby_ask[i] in babl:
                babl = babl.replace(baby_ask[i], f"{i}")

        if not babl.isdigit():
                continue
        
        asks = 1
        for i in range(1, len(babl)):
            if babl[i-1] == babl[i]:
                asks = 0
        answer += asks
                
    return answer

# 코드 참고 용
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer

# 문자열 나누기
def solution(s):
    answer = 0

    

    return answer


a = solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa", "ayawooaya"])
print(a)