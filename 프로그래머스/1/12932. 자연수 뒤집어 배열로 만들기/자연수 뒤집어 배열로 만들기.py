def solution(n):
    str_n = str(n)
    list_n = []
    answer = []
    for i in range(len(str_n)) :
        list_n.append(str_n[i])
    for i in reversed(list_n) :
        answer.append(int(i))
    return answer