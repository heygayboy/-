#coding=utf-8

shuru = raw_input().split(' ')
shuru = map(int, shuru)
n = shuru[0]
k = shuru[1]

shuru = raw_input().split(' ')
liebiao = map(int, shuru)

liebiao.sort(reverse= True)
min_pre = None
for i in range(k):
    if min_pre == None:
        min = liebiao.pop()
        print(min)
        if min == 0:
            break
        min_pre = min
    else:
        min = liebiao.pop()
        print(min - min_pre)
        if min - min_pre == 0:
            break
        min_pre = min


