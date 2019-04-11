#coding=utf-8
'''
最近一款吃鸡类型的游戏火爆全球。在组队模式下，你可以邀请自己的好友组建自己的小队，
并选择是否填充（是否同意和非好友游玩），然后加入游戏。
现在有A个单人队伍，B个双人队伍，C个三人队伍，D个四人队伍，并且全都同意填充，
请问最多能组成多少个四人队伍。

'''
import sys

num_team = int(raw_input())
questions = []


def zudui(question_list):
    res = 0
    res += question_list[3]
    if question_list[0] >= question_list[2]:
        res += question_list[2]
        ones_left = question_list[0]-question_list[2]
        if question_list[1]%2 != 0:
            if ones_left > 0:
                res += question_list[1]/2 + 1
            else:
                res += question_list[1]/2
        else:
            res = res + question_list[1]/2  + ones_left/4
    else:
        res += question_list[0]
        res += question_list[1]/2
    return res


for i in range(int(num_team)):
    new_list = sys.stdin.readline().strip().split(' ')
    line = map(int, new_list)
    questions.append(line)

for question in questions:
    res = zudui(question)
    print(res)

