def solution(s) :
    list_s = []
    upper = []
    lower = []
    for i in range(len(s)) :
        list_s.append(s[i])
    list_s = list(reversed(sorted(list_s)))
    for i in list_s :
        if i.isupper() :
            upper.append(i)
        else : 
            lower.append(i)
    lower = lower + upper
    answer = ''.join(lower)
    return answer