def solution(n):
    answer = ''
    watermelone = "수박"
    if n % 2 == 0 :
        answer += watermelone * (n // 2)
    else : 
        answer += (watermelone * (n // 2) + watermelone[0])
    return answer