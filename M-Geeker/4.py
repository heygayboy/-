length = int(raw_input())

shuru1 = raw_input().split(' ')
shuru1 = map(int, shuru1)
max_num = 0

for i in range(length):
    flag = 0
    res = []
    res.append(shuru1[i])
    for j in range(i+1, length):
        if shuru1[j] - res[-1] == 1:
            res.append(shuru1[j])
        else:
            if flag == 0:
                continue
            else:
                max_num = max(max_num, sum(res))
                break
    max_num = max(max_num, sum(res))

print(max_num)