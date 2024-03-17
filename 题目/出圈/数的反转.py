list=[]
a=int(input())
for i in range(a):
    b=input()
    list.append(b)

for i in list:
    string = str(i)
    print(int(string[::-1]))