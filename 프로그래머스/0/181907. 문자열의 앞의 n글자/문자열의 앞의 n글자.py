def solution(my_string, n):
    count = 0
    answer = ''
    for i in my_string :
        if count != n :
            count += 1
            answer += i
    return answer