"""
列表每两个相邻的数，如果前面的比后面的大，则交换这两个数。
一趟排序完成后，则无序区减少一个数，有序区增加一个数。
"""
def bubble_sort(li):
    for i in range(len(li)-1):
        change=False
        for j in range(len(li)-1-i):
            if li[j+1] < li[j]:
                li[j+1], li[j] = li[j], li[j+1]
                change=True
        if not change:
            break
    print(li)


def select_sort(li):
    new_list = []
    for i in range(len(li)):

        min_val=min(li)
        new_list.append(min_val)
        li.remove(min_val)
    print(new_list)
def select_sort_advance(li):
    for i in range(len(li)):
        loc=i  # 无序区位置
        for j in range(i+1, len(li)):
            if li[j]<li[loc]:
                loc=j
        li[i], li[loc] = li[loc], li[i]
    print(li)



li=[1, 85, 6, 78, 1, 545, 45]
#select_sort(li)
#bubble_sort(li)
select_sort_advance(li)