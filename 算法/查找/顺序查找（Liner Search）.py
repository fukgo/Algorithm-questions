import time

# index()为线性查找
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        else:
            return None
"""时间复杂度O(n)"""
li = [1,5,9,84,511]


start = time.time()
a = linear_search(li, 5)
print(a)
end = time.time()
print(end-start)