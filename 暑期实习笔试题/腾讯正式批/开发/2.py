#coding=utf-8
'''
牛牛和羊羊正在玩一个纸牌游戏。这个游戏一共有n张纸牌, 第i张纸牌上写着数字ai。
牛牛和羊羊轮流抽牌, 牛牛先抽, 每次抽牌他们可以从纸牌堆中任意选择一张抽出, 直到纸牌被抽完。
他们的得分等于他们抽到的纸牌数字总和。
现在假设牛牛和羊羊都采用最优策略, 请你计算出游戏结束后牛牛得分减去羊羊得分等于多少。
'''
n = input()
shuru = raw_input().split(' ')
ai = map(int, shuru)
# n = 2
# ai = [3,1]

ai.sort(reverse= True)

niuniu = 0
yangyang = 0

for i in range(len(ai)):
    if i % 2 == 0:
        niuniu = niuniu + ai[i]
    if i % 2 == 1:
        yangyang = yangyang + ai[i]

print(niuniu - yangyang)
