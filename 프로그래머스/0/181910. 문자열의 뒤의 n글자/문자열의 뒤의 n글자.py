def solution(my_string, n):
    answer = ''
    for i, x in zip(my_string[::-1], range(n)) :
        if x != n :
            answer += i
    
    return answer[::-1]