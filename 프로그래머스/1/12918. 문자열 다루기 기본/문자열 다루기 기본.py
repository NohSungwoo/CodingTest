def solution(s):
    if len(s) == 4 or len(s) == 6 : 
        for i in s :
            if i.isalpha() :
                return False 
            else : 
                pass
        return True
    return False