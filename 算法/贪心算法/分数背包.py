# 每个商品元组表示商品的价格和重量
gods=[(50, 2), (60, 4), (20, 1), (3, 0.1)]
gods.sort(key=lambda x: x[0]/x[1], reverse=True)
print(gods)
#[(3, 0.1), (50, 2), (20, 1), (60, 4)]
def get(gods, w):
    """
    :param gods:   货物列表
    :param w: 背包最大承受重量
    :return:
    """
    total_value=0
    return_li = [0 for i in range(len(gods))]
    for i, (price, weight) in enumerate(gods):
        if w>weight:
            return_li[i]=1
            total_value+=price
            w-=weight
        else:
            return_li[i]=w/weight
            total_value+=return_li[i]*price
            w=0
            break
    return total_value, return_li
x = get(gods, 5)
print(x)

gods.sort(reverse=True)
print(5//2, )
from collections import defaultdict
d=defaultdict()
