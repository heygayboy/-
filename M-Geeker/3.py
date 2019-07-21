import pandas as pd

def minmi(a, b):
    return min(a, b)

shuru1 = raw_input().split(' ')
shuru1 = map(int, shuru1)
cookie_total = shuru1[0]
kaoxiang_total = shuru1[1]
limit_time = shuru1[2]
max_cook = shuru1[3]

# class Kaoxiang():
#     def __init__(self, x, l):
#         self.size = x
#         self.life = l
#         self.nengkao = min(self.size, self.life)

kaoxiang_list = []
kaoxiang_index = []
for _ in range(kaoxiang_total):
    shuru2 = raw_input().split(' ')
    shuru2 = map(int, shuru2)
    shuru2.append(min(shuru2[0], shuru2[1]))
    kaoxiang_index.append(shuru2[0])
    kaoxiang_list.append(shuru2[1:])

kaoxiang = pd.DataFrame(kaoxiang_list, index=kaoxiang_index , columns=['life', 'nengkao'])
# kaoxiang.sort_values(by='nengkao', ascending=False)
# kaoxiang.sort_values(['nengkao'],ascending=False,inplace=True)


cookie_num = 0
time = 0


while cookie_num < cookie_total:
    time = time + 1
    kaoxiang.sort_values(['nengkao'], ascending=False, inplace=True)
    cook_df = kaoxiang.head(max_cook)
    cookie_num = cookie_num + cook_df['nengkao'].sum()
    cook_df['life'] = cook_df['life'] - cook_df['nengkao']

    cook_df['nengkao'] = cook_df.apply(lambda row: minmi(row['nengkao'], row['life']), axis=1)

if cookie_num >= cookie_total:
    print('Yes')
    print(time)
else:
    print('No')
    print(time)