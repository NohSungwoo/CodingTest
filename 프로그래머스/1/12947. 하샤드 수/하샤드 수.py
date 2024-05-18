def solution(x):
    str_x = str(x)
    count = len(str(x))
    hashard = 0
    for i in range(count) :
        hashard += int(str_x[i])
    if x % hashard == 0 :
        answer = True
    else :
        answer = False
    return answer