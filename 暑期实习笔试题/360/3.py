#coding=utf-8
from __future__ import print_function
'''
给定一个长度为N的序列A1到AN，现在要对序列进行M次操作，
每次操作对序列的前若干项进行升序或降序排列，求经过这M次操作后得到的序列。
第一行包含两个整数N和M，1≤N，M≤105。
第二行包含N个空格隔开的整数A1到AN，1≤Ai≤109。
接下来M行，每行包含两个整数t和x，0≤t≤1，1≤x≤N。若t=0，则表示对A1到Ax进行升序排列；
若t=1，则表示对A1到Ax进行降序排列。操作执行顺序与输入顺序一致。'''
import sys


line = sys.stdin.readline().strip().split(' ')
length = int(line[0])
operater_num = int(line[1])
line2 = sys.stdin.readline().strip().split(' ')
N = map(int, line2)


operaters = []
for _ in range(operater_num):
    new_list = sys.stdin.readline().strip().split(' ')
    operater = map(int, new_list)
    operaters.append(operater)


for operater in operaters:
    if operater[0] == 0:
        N[0: operater[1]] =sorted(N[0: operater[1]])
    if operater[0] == 1:
        N[0: operater[1]] = sorted(N[0: operater[1]], reverse=True)

for num in N:
    print(num, end=' ')



