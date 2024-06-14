def solution(n):
    answer = [n]
    
    while n != 1 :
        if n % 2 == 1 :
            n = n * 3 + 1
        else : 
            n = n // 2
        answer.append(n)    
    
    return answer