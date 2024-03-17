target = input().lower()
txt_list = input().split()
count = 0
direction = 0
for i in txt_list:
    if target == i.lower():
        count+=1
        if direction ==0:
            direction=i
if count>0:
    print(count, direction)
else:
    print(-1)