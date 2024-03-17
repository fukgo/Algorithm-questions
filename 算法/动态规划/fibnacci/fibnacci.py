"""
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765
"""
# m为第m项


"""
fib(5)=f(4)+f(3)    
 fib(4)=f(3)+f(2)
  fib(3)=f(2)+f(1)
 fib(3)=f(2)+f(1)

fib(3)=f(2)+f(1)
fib(2)=f(1)+f(0)
"""
class Solution:
    def fibnacci(self, m):
        if m == 1 or m == 2:
            return 1
        else:
            return self.fibnacci(m-1)+self.fibnacci(m-2)


    def fibnacci_no_recurision(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b= b, a+b
        return a
    def fibnacci_no_recurision_(self, n):
        f = [0, 1, 1]
        if n>2:
            for i in range(n-2):
                num = f[-1] + f[-2]
                f.append(num)
        return f[n]

x = Solution()
print(x.fibnacci(20))
print(x.fibnacci_no_recurision(20))
print(x.fibnacci_no_recurision_(20))
