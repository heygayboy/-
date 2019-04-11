

def split_num(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if k > 0:
        return split_num((n + 1) / 2, k - 1) + 1
    return n

shuru = raw_input().split(' ')
shuru = map(int, shuru)
n = shuru[0]
k = shuru[1]
re = split_num(n, k)
print(re)
