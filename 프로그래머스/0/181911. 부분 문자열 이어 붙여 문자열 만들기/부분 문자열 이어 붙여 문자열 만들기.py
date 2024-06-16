def solution(my_strings, parts):
    answer = ''
    count = 0
    
    for part in parts :
        answer += my_strings[count][part[0] : part[1] + 1]
        count += 1
    return answer