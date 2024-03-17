nums_line = int(input())
columns = int(input())
T = []
for _ in range(nums_line):
    for _ in range(columns):
        T.append(str(input()))
T.sort()
print(''.join(T))

T=int(input())
for i in range(T):
    n=int(input())#第i组数据的字符串个数
    m=[]#定义存储第i组数据的空列表
    for i in range(n):#输入并存储第i组数据
        m.append(str(input()))
    for j in range(n):##两个循环比较，字典序小的排在前面，整理第i组数据
        for k in range(j+1,n):
            if m[j]+m[k]>m[k]+m[j]:
               h=m.pop(k)
               m.insert(k,m[j])
               m[j]=h               
    print(''.join(m))#输出整理后的每组数据