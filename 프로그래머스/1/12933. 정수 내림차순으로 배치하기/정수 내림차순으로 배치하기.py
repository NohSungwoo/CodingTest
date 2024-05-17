def solution(n):
    str_n = str(n)
    list_n = list(reversed(sorted(str_n)))
    answer = ""
    for i in list_n :
        answer += i
    return int(answer)