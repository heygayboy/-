#coding=utf-8

shuru = raw_input().split(' ')
shuru = map(int, shuru)
n = shuru[0]
k = shuru[1]

shuru = raw_input().split(' ')
liebiao = map(int, shuru)

liebiao.sort()

h = 0
pre_h = -1

for i in range(k):
    if h >= n:
        print(0)
        continue
    if pre_h < 0:
        print(liebiao[0])
    else:
        print(liebiao[h] - liebiao[pre_h])
    current = liebiao[h]
    pre_h = h
    while (liebiao[h] == current and h < n):
        h = h + 1
