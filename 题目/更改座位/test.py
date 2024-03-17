
# 傻逼gpt，错的
from collections import defaultdict

def min_swaps_to_sort(lst1, lst2):
    if sorted(lst1) != sorted(lst2):
        return -1  # 如果两个列表中的元素不一样，无法通过交换得到相同列表

    index_map = defaultdict(int)
    for i, val in enumerate(lst1):
        index_map[val] = i  # 记录 lst1 中每个元素的索引

    swaps = 0
    for i in range(len(lst2)):
        if lst2[i] != lst1[i]:  # 如果两个列表对应位置的元素不同
            swaps += 1  # 需要交换次数加一
            # 交换 lst2[i] 和 lst2[index_map[lst1[i]]] 的位置
            lst2[i], lst2[index_map[lst1[i]]] = lst2[index_map[lst1[i]]], lst2[i]
            # 更新 lst1 中元素对应的索引值
            index_map[lst2[index_map[lst1[i]]]] = index_map[lst1[i]]
            index_map[lst1[i]] = i
            print(lst2)

    return swaps

# 测试例子
list1 = ["a", "b", "c", "d"]
list2 = ["d", "c", "b", "a"]

result = min_swaps_to_sort(list1, list2)
print(f"需要最小的交换次数为：{result}")
