#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys

# line_str = sys.stdin.readline().split()
# line = map(int,line_str)
#
# if not line:
#     print (0)

line = [3,4,6,5,5,7,8]
pre = line[0]

flag = 1
times = 0

for i in range(1, len(line)):
    num = line[i]
    if num >= pre:
        pre = num
        continue
    else:
        if times <= 1:
            if line[i-2] <= num:
                line[i -1] = line[i-2]
                times = times + 1
                continue
            else:
                flag = 0
                break
        else:
            flag = 0
            break

print(flag)
