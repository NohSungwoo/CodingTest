def solution(price, money, count):
    total_price = 0
    for i in range(count + 1) :
        total_price += i * price
    if money - total_price >= 0 :
        return 0
    else : 
        return abs(money - total_price)