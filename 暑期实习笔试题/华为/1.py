#coding=utf-8
from __future__ import print_function
import sys

num = int(raw_input())
lines = []

line1 = sys.stdin.readline().strip().split(',')
line1 = map(int, line1)
line2 = sys.stdin.readline().strip().split(',')
line2 = map(int, line2)
length1 = len(line1)
length2 = len(line2)
i = 0
j = 0

res = []
while (i + num <= length1) and (j + num <= length2):
    res.extend(line1[i: i + num])
    res.extend(line2[j: j + num])
    i = i + num
    j = j + num

if i + num  > length1:
    res.extend(line1[i:])
    res.extend(line2[j:])
else:
    res.extend(line1[i: i + num])
    i = i + num
    res.extend(line2[j:])
    res.extend(line1[i:])

for number in res:
    print(number, end=',')
print ()

