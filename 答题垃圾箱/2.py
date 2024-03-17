#n 个摊位和m 次询问
n, m = str(input()).split()
n = int(n)
m = int(m)
num = 10000
n_list = []
result_list=[]
for i in range(2, num):
    re = False
    for j in range(2, i):
        if i % j == 0:
            re = True
            break
    if re == False and len(n_list)<n:
        n_list.append(i)


for i in range(m):
    x, y, z =str(input()).split()
    x, y, z = int(x),int(y),int(z)
    if x == 1:
        n_list[y-1]+=z
    else:
        result_list.append(sum(n_list[y-1:z]))

for i in result_list:
    print(i)






