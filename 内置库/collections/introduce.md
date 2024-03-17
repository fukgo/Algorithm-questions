1. 介绍
collections是Python内建的一个集合模块，提供了许多有用的集合类和方法。

可以把它理解为一个容器，里面提供Python标准内建容器 dict , list , set , 和 tuple 的替代选择。

import collections

print(dir(collections))
里面有许多方法，我们只介绍常用的方法。

2.常用方法
namedtuple() ： 创建一个命名元组子类的工厂函数
deque ： 　　　高效增删改双向列表，类似列表(list)的容器，实现了在两端快速添加(append)和弹出(pop)
defaultdict ： 当字典查询时，为key不存在提供一个默认值。
OrderedDict ： 有序词典，就是记住了插入顺序
Counter ： 计数功能
1. namedtuple() 命名元组
2. deque 双端队列
3. defaultdict 默认值字典
4. OrderedDict 有序字典
5. Counter 计数