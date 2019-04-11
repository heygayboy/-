#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

def min_dis(target_a, num_of_points, points, dis):
    if num_of_points == 1:
        return dis
    if target_a <= points[0]:
        num_pos = 0
    elif target_a >= points[num_of_points - 1]:
        num_pos = num_of_points - 1
    else:
        i = 0
        j = num_of_points - 1
        while j-i > 1:
            p = (j + i) / 2
            if points[p] > target_a:
                j = p
            elif points[p] < target_a:
                i = p
            else:
                num_pos = p
        if target_a - points[i] <= points[j] - target_a:
            num_pos = i
        else:
            num_pos = j

        min_dis(target_a + points[num_pos], num_of_points - 1, points.pop(num_pos), dis)



if __name__ == "__main__":
    # 读取第一行的n
    line1 = sys.stdin.readline().split()
    line2 = sys.stdin.readline().split()

    num_of_points = int(line1[0])
    target_a = int(line1[1])

    points = map(int,line2)
    dis =0
    res = min_dis(target_a, num_of_points, points, dis)






