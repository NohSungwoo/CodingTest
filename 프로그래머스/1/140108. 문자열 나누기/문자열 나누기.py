
def solution(s):
    answer = 0
    first_string = s[0]
    equal_first = 0
    none_first = 0

    for i in range(len(s)):
        if s[i] == first_string:
            equal_first += 1
        else:
            none_first += 1

        if equal_first == none_first:
            answer += 1
            if len(s) > none_first + equal_first:
                first_string = s[none_first + equal_first]
        elif i == len(s) - 1:
            answer += 1
        
    return answer
