def solution(rsp):
    answer = ''
    dict_rsp = {'2' : '0', 
                '0' : '5', 
                '5' : '2'}
    for i in rsp :
        answer += dict_rsp[i]
    return answer