def solution(n, m):
    gcd = 1
    for x in range(1, min(n, m) + 1):
        if n % x == 0 and m % x == 0:
            gcd = x 
                
    answer = [gcd, n * m // gcd]
    return answer