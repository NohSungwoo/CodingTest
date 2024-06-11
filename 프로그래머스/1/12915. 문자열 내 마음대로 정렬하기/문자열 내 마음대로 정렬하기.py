def solution(strings, n):
    # string의 n번째 글자를 기준으로 정렬해라
    # dict를 str sort순으로 연결
    answer = []
    answer2 = []
    
    for string in strings :
        answer.append(string[n] + string)
    answer.sort()
    
    for string in answer :
        answer2.append(string[1:len(string)])
    
    return answer2