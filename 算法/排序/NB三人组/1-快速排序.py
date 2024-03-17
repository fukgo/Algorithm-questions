"""快速排序：快
思路：1，取一个元素（第一个元素），使元素p归位
2，列表被p分成两部分，左边都比p小，右边都比p大
3，递归完成排序"""

"""
def quick_sort(data, left, right):
    if left<right:
        mid = partition(data, left, right)
        quick_sort(data, left, right-1)
        quick_sort(data, mid+1, right)"""
def partition(li, left, right):
    tmp=li[left]
    while left<right:
        while li[right]>=tmp and left<right:
            right-=1  # 往左走一步
        li[left]=li[right]  # 把右边的值写到左边的空位上
        print(li)
        while li[left]<=tmp and left<right:
            left+=1
        li[right]=li[left]  # 把左边的值写到右边的空位上
        print(li)
    li[left]=tmp  # or li[right]=tmp
    return left
def quick_sort(li, left, right):
    if left<right:  # 至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)

li=[5,7,4,6,3,1,2,9,8, 5.26]
quick_sort(li, 0, len(li)-1)
"""时间复杂度：O(n*lgn)"""



