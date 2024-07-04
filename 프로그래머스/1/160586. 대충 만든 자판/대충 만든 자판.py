def solution(keymap, targets):

    dic = {}

    for index, keys in enumerate(keymap):
        for i, str in enumerate(keys):
            if str in dic:
                dic[str] = min(dic[str], i + 1)
            else:
                dic[str] = i + 1
    results = []

    for target in targets:
        count = 0
        for str in target:
            if str in dic:
                count += dic[str]
            else:
                count = -1
                break
        results.append(count)

            
    return results