# 신규 아이디 추천 코드
def solution(new_id):
    result_str = "~!@#$%^&*()=+[{]}:?,<>/"
    
    new_id = new_id.lower()
    
    for s in result_str:
        new_id = new_id.replace(s, "")
    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    new_id = new_id.strip('.')
    
    if new_id == '':
        new_id = 'a'
    
    if len(new_id) > 15:
        new_id = new_id[:15].strip('.')
    
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id

# 둘만의 암호
def solution(s, skip, index):
    answer = ''
    for strs in s:
        n = 1
        result = ''
        while n < index+1:
            r = ord(strs) + 1
            result = chr(r-122+96) if r > 122 else chr(r)
            if result not in skip:
                n += 1
            strs = result
        answer += result

    return answer

# 대충 만든 자판
def solution(keymap, targets):
    answer = []
    
    for target in targets:
        num = 0
        for s in target:
            min_target = []
            for key_list in keymap:
                if s in key_list:
                    min_target.append(key_list.find(s) +1)
            if len(min_target) != 0:
                num += min(min_target)
            else:
                num = -1
                break
        answer.append(num)

    return answer

def solution(ingredient):
    answer = 0
    food = "1231"
    ingre = ''.join(map(str,ingredient))
    
    while food in ingre:
        answer += ingre.count(food)
        ingre = ingre.replace(food, '')

    return answer

a = solution([2,2,3,1,2,3,2,1,2,2,3,1,2,3,2,1,1,2,3,2,1,2,3,1,2,2,3,1,1,2,3,2,1,3,2,1,3,2,1,3,2,])
print(a)
