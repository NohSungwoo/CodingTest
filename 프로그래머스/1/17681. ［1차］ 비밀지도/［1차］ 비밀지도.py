def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []

    for a, b in zip(arr1, arr2) :
        arr1_bin.append(bin(a))
        arr2_bin.append(bin(b))
        
    arr1 = []
    arr2 = []
    
    for a, b in zip(arr1_bin, arr2_bin) :
        arr1.append(a[2:])
        arr2.append(b[2:])
    
    for a, b in zip(arr1, arr2) :
        answer.append(int(a) + int(b))
    
    wall_list = []
    
    for i in answer :
        wall = ''
        if len(str(i)) < n :
            wall += ' ' * (n - len(str(i)))
        for j in str(i) :
            if 1 <= int(j) :
                wall += '#'
            else :
                wall += ' '
        wall_list.append(wall)
    return wall_list