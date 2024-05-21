def solution(arr):
    answer = []
    if len(arr) >= 2 :
        arr.remove(arr[arr.index(min(arr))])
        answer = arr
    else :
        answer = [-1]
    return answer