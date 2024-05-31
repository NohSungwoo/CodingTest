def solution(price):
    if price >= 500000 :
        price -= price * 0.2
        return int(price)
    elif price >= 300000 :
        price -= price * 0.1
        return int(price)
    elif price >= 100000 :
        price -= price * 0.05
        return int(price)
    return price 
