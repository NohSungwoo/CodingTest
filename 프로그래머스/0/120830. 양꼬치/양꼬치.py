def solution(n, k):
    answer = 0
    sheep = 12000
    drink = 2000
    answer += (sheep * n) + (drink * k)
    answer -= (n // 10) * drink
    return answer