#coding=utf-8
from __future__ import print_function


def add_zero(string, zero_nums):
    add_zero_string = ['0'] * zero_nums
    add_zero_string = ''.join(add_zero_string)
    new_string = string + add_zero_string
    return new_string

shuru = raw_input().split(' ')
shuru = shuru[1:]

# shuru = ['abc', '123456789']

res = []
for i in range(len(shuru)):
    string = shuru[i]
    if len(string) < 8:
        new_string = add_zero(string, 8-len(string))
        res.append(new_string)
    else:
        start = 0
        while start + 8 < len(string):
            res.append(string[start: start+8])
            start = start + 8
        remained = string[start:]
        new_string = add_zero(remained, 8 - len(remained))
        res.append(new_string)

res.sort()
for re in res:
    print(re, end=' ')