from collections import defaultdict
now = ["d","b","b","a"]
target = ["a","b","c","d"]
#a = input().split()
#b = input().split()
def min_swap(lst_now, lst_goal):
    if sorted(lst_now) != sorted(lst_goal):
        print(sorted(lst_now),"\n",sorted(lst_goal))
        return -1

    index_map = defaultdict(int)
    for key, val in enumerate(lst_goal):
        index_map[val] = key
    #print(index_map)
    swap = 0
    for i in range(len(lst_now)):
        if lst_now[i] != lst_goal[i]:
            swap += 1
            ind = index_map[lst_now[i]]
            lst_now[i], lst_now[ind] = lst_now[ind], lst_now[i]
    return swap

n = min_swap(now, target)
print(n)