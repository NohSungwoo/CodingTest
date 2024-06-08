def solution(my_string, is_prefix):
    answer = 0
    count = 0
    for a, b in zip(my_string, is_prefix) :
        if a == b :
            count += 1
        if count == len(is_prefix) :
            return 1
    return answer
        