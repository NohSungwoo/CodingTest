def solution(n):
    answer = 0
    for i in range(1, n + 1) :
        if n % i == 0 :
            x = n // i
        if i * x == n :
            answer += 1
        elif x * i == n :
            abswer += 1
            
           
    return answer