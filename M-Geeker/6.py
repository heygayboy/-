shuru1 = raw_input().split(' ')
shuru1 = map(int, shuru1)
lianxice_num = shuru1[2]
shuru_num = shuru1[1]
time = shuru1[0]
plan = [[] for _ in range(time)]
res = []

def add_plan(plan, L, R, v):
    for i in range(L, R+1):
        plan[i].append(v)
    return plan


def delete_plan(plan, L, R, v):
    for i in range(L, R+1):
        if v in plan[i]:
            plan[i].remove(v)
    return plan

def search(plan, L, R):
    plans = []
    for i in range(L, R + 1):
        for j in range(len(plan[i])):
            if plan[i][j] not in plans:
                plans.append(plan[i][j])
    return len(plans)

for _ in range(shuru_num):
    shuru2 = raw_input().split(' ')
    shuru2 = map(int, shuru2)
    opt = shuru2[0]
    L = shuru2[1] - 1
    R = shuru2[2] - 1
    if len(shuru2) == 4:
        v = shuru2[3]

    if opt == 1:
        plan = add_plan(plan, L, R, v)
    elif opt == 2:
        plan = delete_plan(plan, L, R, v)
    else:
        plan_num = search(plan, L, R)
        res.append(plan_num)

for plan_num in res:
    print plan_num
