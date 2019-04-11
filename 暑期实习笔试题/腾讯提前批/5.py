#coding=utf-8


from __future__ import print_function
import sys


line1 = raw_input()
line2 = sys.stdin.readline().split()

num_of_points = int(line1)

points = map(int, line2)

for i in range(1, num_of_points):
    for j in range(0, i):
        if j == 0:
            min_num = points[i] - points[0]
            pos = 0
        if abs(points[i] - points[j] < min_num):
            min_num = abs(points[i] - points[j])
            pos = j
    print(min_num, j, sep = ' ', end= '\n')