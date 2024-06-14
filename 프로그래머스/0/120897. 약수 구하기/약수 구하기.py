def solution(n):
    answer = []
    for divisior in range(1, n + 1) :
        if n // divisior == n / divisior :
            answer.append(divisior)
    return answer