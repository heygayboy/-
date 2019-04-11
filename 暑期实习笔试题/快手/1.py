#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys
nums_len = sys.stdin.readline()
line_str = sys.stdin.readline().split()
line = map(int,line_str)

def print_odd_times_num1(arr):
    odd = 0
    for i in arr:
        odd ^= i
    return odd

print(print_odd_times_num1(line))