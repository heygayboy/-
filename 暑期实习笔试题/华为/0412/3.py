#coding=utf-8
from __future__ import print_function

import numpy as np


shuru = raw_input().split(' ')
n = int(shuru[0])
m = int(shuru[1])

array = []
for i in range(n):
    shuru = raw_input().split(' ')
    shuru = map(int, shuru)
    array.append(shuru)

zuobiao = raw_input().split(' ')
X = int(zuobiao[0])
Y = int(zuobiao[1])
Z = int(zuobiao[2])
W = int(zuobiao[3])


dp = np.zeros((n, m))
dp[0][0] = 1

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if i == 0:
            if array[i][j] > array[i][j-1]:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = 0
        elif j == 0:
            if array[i][j] > array[i-1][j]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = 0
        else:
            if array[i][j] > array[i - 1][j] and array[i][j] > array[i][j-1]:
                dp[i][j] = dp[i - 1][j] + dp[i][j-1]
            elif array[i][j] > array[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif array[i][j] > array[i][j-1]:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = 0

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if i == n-1 and j == m-1:
            continue
        if i == n-1:
            if array[i][j] > array[i][j+1]:
                dp[i][j] = dp[i][j] + dp[i][j+1]
        elif j == n-1:
            if array[i][j] > array[i+1][j]:
                dp[i][j] = dp[i][j] + dp[i+1][j]
        else:
            if array[i][j] > array[i+1][j] and array[i][j] > array[i][j+1]:
                dp[i][j] = dp[i+1][j] + dp[i][j+1] + dp[i][j]
            elif array[i][j] > array[i+1][j]:
                dp[i][j] = dp[i + 1][j] + dp[i][j]
            elif array[i][j] > array[i][j] > array[i][j+1]:
                dp[i][j] = array[i][j+1] + dp[i][j]

print ((dp[X][Y] * dp[Z][W])%10)





