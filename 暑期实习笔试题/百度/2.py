#coding=utf-8
'''
给定一个仅由小写字母组成且长度不超过106的字符串，
将首字符移到末尾并记录所得的字符串，不断重复该操作，
虽然记录了无限个字符串，但其中不同字符串的数目却是有限的，
那么一共记录了多少个不同的字符串？
'''
import sys
A = raw_input()
B = raw_input()
Q = int(raw_input())


def find(target, B):
    res = 0
    for i in range(len(target) - len(B)+1):
        temp = target[i: i+len(B)]
        if temp == B:
            res += 1
    return res

landr = []
for _ in range(Q):
    landr.append(sys.stdin.readline().strip().split(' '))

for x in landr:
    l = int(x[0]) - 1
    r = int(x[1]) - 1
    # print(l, r)
    target = A[l:r+1]
    print(find(target, B))