def solution(my_string):
    answer = [int(num) for num in my_string if num.isdigit()]
    answer.sort()
    
    return answer