num = input().strip()
li = []
d = {'A': 0,'B': 0,'C': 0,'D':0,}
for i in range(int(num)):
    x = input()
    for j in d:
        if x == j:
            d[j]+=1
print(d.keys())
m=max(d.keys(),key=(lambda x:d[x]))
M =max(d.keys(), key=(lambda x:d[x]))
print(m, d[m])
