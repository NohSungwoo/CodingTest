def solution(array):
    array = list(sorted(array))
    answer = array[len(array) - (len(array) // 2) - 1]
    return answer
