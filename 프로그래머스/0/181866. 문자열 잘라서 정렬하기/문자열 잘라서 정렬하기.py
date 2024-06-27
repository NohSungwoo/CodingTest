def solution(myString):
    answer = sorted(myString.replace('x', ' ').split())
    return answer