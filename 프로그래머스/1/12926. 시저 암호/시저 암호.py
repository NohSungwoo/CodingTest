def solution(s, n):
    lower_dict = 'abcdefghijklmnopqrstuvwxyz'
    upper_dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    answer = ''
    
    for char in s:
        if char == ' ':
            answer += ' '
        elif char.islower():
            answer += lower_dict[(lower_dict.index(char) + n) % 26]
        elif char.isupper():
            answer += upper_dict[(upper_dict.index(char) + n) % 26]
    
    return answer
