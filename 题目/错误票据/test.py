i = int(input(""))
li = []
A,B=0,0
for _ in range(i):
    x = input("")
    y = x.split()
    for __ in y:
        li.append(int(__))
for i in range(len(li)-1):
    exchange=False
    for j in range(len(li)-i-1):
        if li[j]>li[j+1]:
            li[j], li[j+1]=li[j+1], li[j]
            exchange=True
    if not exchange:
        break
for i in range(li[0], li[-1]+1):
    if li.count(i) == 0:
        A=i
    elif li.count(i) == 2:
        B=i
print(A,B)







