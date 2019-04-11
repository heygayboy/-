#coding=utf-8
'''
给定一个1到N的排列A1到AN，每次可以将排列的第一个数移到排列的末尾，
假设经过若干次移动后得到排列B1到BN，那么|B1-1|+|B2-2|+|B3-3|+...+|BN-N|的最小值是多少？
样例解释:
{4 3 1 5 2}经过两次移动后得到排列{1 5 2 4 3}，此时|B1-1|+|B2-2|+|B3-3|+|B4-4|+|B5-5|取得最小值。
'''
import sys
import numpy as np

length = int(raw_input())
new_list = sys.stdin.readline().strip().split(' ')
N = map(int, new_list)


jianshu = np.arange(1, length+1)
jianshu = np.concatenate(np.array([jianshu] * length))
beijianshu = np.array(N)
min = None


for i in range(length):
    value = np.sum(np.abs(beijianshu - jianshu[i:i+length]))
    if not min:
        min = value
    else:
        if value < min:
            min = value
print(min)
