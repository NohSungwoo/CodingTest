def solution(myString):
    answer = []
   
    for char in myString.split('x') :
        answer.append(len(char))
    return answer