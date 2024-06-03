def solution(arr):
    answer = [arr.pop()]
    for i in arr[::-1] :
        if arr[-1] == answer[-1] :
            arr.pop()
        else : 
            answer.append(arr.pop())
    return answer[::-1]
