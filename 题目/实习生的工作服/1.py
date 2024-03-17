n, m = input().split(' ')
num_people = list(map(int,input().split(' ')))
size_cothes = list(map(int,input().split(' ')))
num_people.sort()
size_cothes.sort()
num = 0
for i in num_people:
    for j in size_cothes:
        if i == j:
            size_cothes.remove(j)
            num += 1
            break
print(num)
