"""
a=int(input("please input the first number："))
b=int(input("please input the second number："))
m,n=a,b #  创建两个变量存储a和b
t=1 #  创建t作为最大公约数的载体
for i in range(2,min(a,b)):
    while (a%i==0 and b%i==0):
       t*=i #  所有公约数累乘起来
       a/=i
       b/=i
print((f"{m},{n}的最大公约数为：{t}"))
"""
import numpy as np
#np.gcd.reduce([15, 25, 35])
num = int(input().strip())
for x in range(num):
    l, r, k = input().split()
    l, r, k = int(l), int(r), int(k)
    li = list(range(l, r+1))
    print(l, r, li)
    for _ in range(k):
        num = None
        for i in range(1, len(li)):
            for j in range(i+1,len(li)):
                li.remove(li.index(i))
                li.remove(li.index(j))
                li.append(li[i]*li[j])
            #a = np.array(li)
            a = np.gcd.reduce(li)
            if num:
                num=a
            if a<num:
                num=a
        if num >1:
            print('MENG')
        else:
            print('CAI')








