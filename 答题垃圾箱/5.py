s = input().split()  # list
i, j = 0, 0
for _ in s:
    if _ == 'L':
        i+=1
    else:
        j+=1
if i>j:
    print('laobanNB!!!')
else:
    print('Jiuzhe???')
