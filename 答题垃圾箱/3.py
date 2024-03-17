"""
10
6 192 114 3 514 1561 545 2151561 151515 15151

4 1 3 2 5
90.00


0
0 3
0 3 6
0 3 6 114
0 3 6 114 192

"""
num = input()
x = input().split()
li = [int(i) for i in x]
d = {}
result=0
for i, j in enumerate(li):
    d[j]=i
li.sort()
for i in li:
    print(d[i]+1, end=' ')
print()
z=1
for i in range(int(num)-1):
    result+=sum(li[0:z])
    z+=1
print(round(result/int(num)))