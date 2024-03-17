num = int(input())
original=input().split()
result = input().split()
co = original.copy()

while i in list(range(num)) and j in list(range(num)):
    original[i], original[j] = original[j], original[i]
    print(i,j)
    print(original)
    j+=1
while i in list(range(1, num)) and j in list(range(num)):
    original[i], original[j] = original[j], original[i]
    print(i,j)
    print(original)

'''
12 13 14 15
23 24 25
34 35
45'''