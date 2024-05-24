import sys
n = input()
list_num = []
max_num = 0
count = 0
for i in range(int(n)) :
    list_num.append(int(sys.stdin.readline()))

list_num = list(reversed(list_num))
for i in list_num :
    if int(i) > max_num :
        max_num = int(i)
        count += 1
print(count)