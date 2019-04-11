#coding=utf-8
from __future__ import print_function

kuohao_start = ['{', '[', '(']
kuohao_end = [')', ']', '}']
stack = []
shuru = raw_input()

i = 0
while i < len(shuru)
    cur = shuru[i]
    if cur < '9' and cur > '1':
        i += 1
        if shuru[i] in kuohao_start:
            stack.append(shuru[i])
            i += 1
            while shuru[i] not in kuohao_end:
                stack.append(shuru[i])




