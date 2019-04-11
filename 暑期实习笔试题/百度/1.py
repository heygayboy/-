#coding=utf-8
'''
给定一个仅由小写字母组成且长度不超过106的字符串，
将首字符移到末尾并记录所得的字符串，不断重复该操作，
虽然记录了无限个字符串，但其中不同字符串的数目却是有限的，
那么一共记录了多少个不同的字符串？
'''

import sys
nums_str = sys.stdin.readline()

# nums_str = 'abab '
str_list = list(nums_str)[:-1]
length = len(str_list)
hash_dict = {}
res = 1
str_yuan = "".join(str_list)
hash_dict[str_yuan] = 1
for _ in range(length):
    new_list = list(str_list.pop())
    new_list.extend(str_list)
    new_str = "".join(new_list)
    if not hash_dict.has_key(new_str):
        res += 1
        hash_dict[new_str] = 1
    str_list = new_list
print(res)

