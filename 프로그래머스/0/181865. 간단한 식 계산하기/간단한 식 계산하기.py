def solution(binomial):
    binomial_list = binomial.split()
    binomial_list[0] = int(binomial_list[0])
    binomial_list[2] = int(binomial_list[2])
    
    if binomial_list[1] == '+' :
        answer = binomial_list[0] + binomial_list[2]
    elif binomial_list[1] == '-' :
        answer = binomial_list[0] - binomial_list[2]
    else :
        answer = binomial_list[0] * binomial_list[2]
    return answer