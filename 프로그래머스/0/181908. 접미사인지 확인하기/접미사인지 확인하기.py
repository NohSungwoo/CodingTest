def solution(my_string, is_suffix):
    answer = 0
    if is_suffix in my_string and my_string[-1] == is_suffix[-1] :
        answer = 1
    return answer