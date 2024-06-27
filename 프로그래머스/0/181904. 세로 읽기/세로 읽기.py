def solution(my_string, m, c):
    my_string = list(my_string)
    tem = ''
    tem_list = []
    answer = ''

    for i, string in zip(range(1, len(my_string) + 1), my_string):

        tem += string

        if i % m == 0:
            tem_list.append(tem)
            tem = ''

    for string in tem_list:
        answer += string[c - 1]

    return answer