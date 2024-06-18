def solution(s):
    result = []
    for word in s.split(' '):
        new_word = ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(word)])
        result.append(new_word)
    return ' '.join(result)


    