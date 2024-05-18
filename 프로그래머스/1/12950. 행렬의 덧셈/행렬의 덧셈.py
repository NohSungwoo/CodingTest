def solution(arr1, arr2):
    c = [] 
    answer = []
    for x in (range(len(arr1))) :
        count = 0
        for y in (range(len(arr1[x]))) :
            count += 1
            c.append(arr1[x][y] + arr2[x][y])
            if count == len(arr1[x]) :
                answer.append(c)
                c = []
    return answer