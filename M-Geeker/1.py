#coding=utf-8

n = raw_input()
n = int(n)
shuru = raw_input().split(' ')
shuru = map(int, shuru)

shuru.sort()
if not shuru:
    print('0')

if n > 1:
    res = float(shuru[0])/float(2**(n-1))
    for i in range(1, len(shuru)):
        res = res + float(shuru[i])/float(2**(n-i))
    print "{:.4}".format(res)
else:
    print(shuru[0])


#coding=utf-8

n = raw_input()
n = int(n)
shuru = raw_input().split(' ')
shuru = map(int, shuru)
if n == 1:
    print "{:.4}".format(shuru[0])

while len(shuru) > 1:
    shuru.sort(reverse= True)
    num1 = shuru.pop(-1)
    num2 = shuru.pop(-1)
    shuru.append(float(num1 + num2)/float(2.0))


print "{:.4}".format(shuru[0])


