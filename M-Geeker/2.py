shuru1 = raw_input().split(' ')
shuru1 = map(int, shuru1)
m = shuru1[0]
n = shuru1[1]

array = []
for _ in range(m):
    shuru2 = raw_input().split(' ')
    shuru2 = map(int, shuru2)
    array.append(shuru2)

res = 0
for i in range(m):
    for j in range(n):
        for z in range(m):
            for k in range(n):
                if i != z and j != k:
                    if array[i][j] * array[z][k] > res:
                        res = array[i][j] * array[z][k]

print(res)

