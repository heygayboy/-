from __future__ import print_function

num = input()

list_num = []
for i in range(num):
    list_num.append(i + 1)

res = []
i = 1
while list_num:
    if i % 2 == 1:
        res.append(list_num.pop(0))
    if i % 2 == 0:
        numb = list_num.pop(0)
        list_num.append(numb)
    i = i + 1

for i in res:
    print(i, end=' ')