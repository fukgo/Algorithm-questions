activity=[(1,4),(3,5),(0,6),(5,7),(3,9),
          (5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]

activity.sort(key=lambda x: x[1])
print(activity)
def avtivity_select(li):
    res = [li[0]]
    for i in range(1, len(li)):
        if li[i][0] >= res[-1][0]:
            res.append(li[i])
    return res
print(avtivity_select(activity))





