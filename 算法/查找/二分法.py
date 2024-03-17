import time

def binary_search(li, val):
    left = 0
    right = len(li)-1
    while left<=right:
        mid = (left+right)//2
        if li[mid]==val:
            return mid
        elif li[mid]>val:
            right=mid-1
        else:
            left=mid+1
    else:
        return 1234
"""时间复杂度O(logn)"""
li = [a for a in range(10000)]

start = time.time()

a = binary_search(li, 55)
print(a)
end = time.time()
print(end-start)



