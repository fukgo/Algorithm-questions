m=13
n=5
num_list=[i for i in range(1, m+1)]
print(num_list[::-1])
#output=3

class Sum:
    def __init__(self, number):
        self.sum=None
        self.number = number

    def count(self):
        self.number = str(self.number)
        sum_list = [int(_) for _ in self.number]
        print(sum_list)
        self.sum = sum(sum_list)
d={}
for i, j in enumerate(num_list):
    s = Sum(j)
    s.count()
    d[i+1]=s.sum
    #print(s.sum)
l=list(d.items())
l.sort(key=lambda x:x[1])
print(l[n-1][1])





