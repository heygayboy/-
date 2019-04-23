#coding=utf-8
'''
在二维平面上有一个无限的网格图形，初始状态下，所有的格子都是空白的。
现在有n个操作，每个操作是选择一行或一列，并在这行或这列上选择两个端点网格，
把以这两个网格为端点的区间内的所有网格染黑（包含这两个端点）。
问经过n次操作之后，共有多少个格子被染黑，显然在众多操作中，很容易重复染色同一个格子，
这个时候只计数一次。

输入第一行包含一个正整数n（1<=n<=10000）.

接下来n行，每行四个整数，x1，y1，x2，y2，分别表示一个操作的两端格子坐标。
（-10^9<=x1,y1,x2,y2<=10^9）,
若x1=x2则是在一列上染色，若y1=y2，则是在一行上染色，保证每次操作是在一行或一列上染色。 
'''


N = int(raw_input())
zuobiaos = []
for _ in range(N):
    shuru = raw_input().split(' ')
    zuobiaos.append(map(int, shuru))

dict = {}
res = 0
for zuobiao in zuobiaos:
    x1, y1, x2, y2 = zuobiao[0], zuobiao[1], zuobiao[2], zuobiao[3]
    if x1 != x2 and y1 != y2:
        continue
    elif x1 == x2 and y1 == y2:
        if dict.has_key((x1, y1)):
            continue
        else:
            res = res + 1
            dict[(x1, y1)] = 1
    elif x1 == x2:
        if y1 > y2:
            temp = y1
            y1 = y2
            y2 = temp
        for num in range(y1, y2+1):
            if dict.has_key((x1, num)):
                continue
            else:
                res = res + 1
                dict[(x1, num)] = 1
    elif y1 == y2:
        if x1 > x2:
            temp = x1
            x1 = x2
            x2 = temp
        for num in range(x1, x2+1):
            if dict.has_key((num, y1)):
                continue
            else:
                res = res + 1
                dict[(num, y1)] = 1
print(res)