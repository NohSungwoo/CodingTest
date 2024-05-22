def solution(a, b):
    answer = 0
    length = len(a)
    for n in range(length):
        answer += a[n] * b[n]      
    return answer