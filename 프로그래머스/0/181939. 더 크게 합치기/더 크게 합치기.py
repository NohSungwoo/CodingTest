def solution(a, b):
    answer = 0
    first_a = ''.join(str(a)) + ''.join(str(b))
    first_b = ''.join(str(b)) + ''.join(str(a))
    
    if int(first_a) > int(first_b) :
        answer += int(first_a) 
    else :
        answer += int(first_b)
    
    return answer