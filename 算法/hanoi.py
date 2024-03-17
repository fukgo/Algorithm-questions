"""
n个盘子时：
1，把n-1个园盘从A经过C移动到B
2，把第n个圆盘从A移动到C
3，把n-1个圆盘经过A移动到C
递推式：h(x) = h*(n-1)+1+h*(n-1)
           = 2*h(x-1)+1
"""
def hanoi(n, a, b, c):
    if n>0:
        hanoi(n-1, a, c, b)
        print("moving from %s to %s" %(a, c))
        hanoi(n-1, b, a, c)
hanoi(3, 'a', 'b', 'c')

