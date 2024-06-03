def solution(n):
    base3 = []
    answer = 0
        
    while n >= 3 : 
        base3.append(n % 3) 
        n = n // 3   
    base3.append(n % 3)
    for i in range(len(base3)) :
        answer += (base3.pop() * (3 ** i)) 
    return answer
