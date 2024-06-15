def solution(numbers, direction):

    if direction == 'right' :
        number_pop = numbers.pop()
        numbers.insert(0, number_pop)
    else :
        number_pop = numbers.pop(0)
        numbers.append(number_pop)
    return numbers