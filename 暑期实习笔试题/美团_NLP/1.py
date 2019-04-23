#coding=utf-8
'''
我们称一个矩阵为黑白矩阵，当且仅当对于该矩阵中每一个位置如(i,j),
其上下左右四个方向的数字相等，即(i-1,j),(i+1,j),(i,j+1),(i,j-1)四个位置上
的数字两两相等且均不等于(i,j)位置上的数字。(超出边界的格子忽略)

现在给出一个n*m的矩阵，我们想通过修改其中的某些数字，使得该矩阵成为黑白矩阵，
问最少修改多少个数字。

'''
from collections import Counter
from itertools import chain


shuru = raw_input().split(' ')
shuru = map(int, shuru)
n = shuru[0]
m = shuru[1]
res = 0
array = []
for _ in range(n):
    shuru = raw_input().split(' ')
    array.append(map(int, shuru))

assert n == len(array) and m == len(array[0])

# array = [[1,1,1], [1,1,1], [1,1,1]]
# m = 3
# n = 3
'''
这里注意a不应该是array[n/2][m/2]，而应该也是一个元素出现最多的值
把一个矩阵拆成两个
分别counter
'''
a = array[n/2][m/2]

for i in range(0, n, 1):
    if i % 2 == 0:
        for j in range(0, m, 2):
            if array[i][j] != a:
                array[i][j] = a
                res = res + 1
    else:
        for j in range(1, m, 2):
            if array[i][j] != a:
                array[i][j] = a
                res = res + 1

array_flatten = list(chain.from_iterable(array))
count_dict = Counter(array_flatten)
max = 0
for key in count_dict.keys():
    if key != a:
        if count_dict[key] > max:
            max = count_dict[key]
            b = key
if max == 0:
    b = None

for i in range(0, n, 1):
    if i % 2 == 0:
        for j in range(1, m, 2):
            if array[i][j] != b:
                array[i][j] = b
                res = res + 1
    else:
        for j in range(0, m, 2):
            if array[i][j] != b:
                array[i][j] = b
                res = res + 1
print(res)

