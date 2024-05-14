def solution(n):
    answer = 0
    a = 1
    while n >= a :
        if n % a == 0 :
            answer += a
            print(a)
        a += 1
    return answer