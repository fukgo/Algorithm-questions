
def back(n):
    money_list=[100, 50, 20, 10, 5, 1]
    num_list=[]
    for i in money_list:
        num, nex = divmod(n, i)
        n-=num*i
        num_list.append(num)
    print(num_list)
back(11)

