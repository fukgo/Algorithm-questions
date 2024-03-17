import random
"""1,random.random(): 返回随机生成的一个浮点数，范围在[0,1)之间"""
print(random.random())
"""2. random.uniform(a, b): 返回随机生成的一个浮点数，范围在[a, b)之间"""
print(random.uniform(4,452))
"""3. random.randint(a,b)：随机生成指定范围内的整数，范围在[a, b)之间"""
print(random.randint(4,425))
"""4. random.randrange([start],stop[,step])：用于从指定范围[a,b]内按指定基数递增的集合中获取一个随机数。"""
a = True
while a:
    a = random.randrange(5, 555, 5)  # =random.choice(range(5,555,5))
    print(a)
    if a >400:
        a = False
"""5. random.choice()：从指定的序列中获取一个随机元素
random.choice()从序列中获取一个随机元素，其原型为random.choice(sequence)，
参数sequence表示一个有序类型。这里说明一下，sequence在Python中不是一种特定的类型，
而是泛指序列数据结构。列表，元组，字符串都属于sequence。
"""
a=[545,45,454,78542,454]
tumple_=tuple(a)
dict = {"nane": "张三", "age": 20, "sex": "男"}
result=random.choice(tumple_)
print(result)

"""6.random.choices(population,weights=None,*,cum_weights=None,k=1)函数
population：集群。
weights：相对权重。
cum_weights：累加权重。
k：选取次数。
作用：从集群中随机选取k次数据，返回一个列表，可以设置权重。

注意：每次选取都不会影响原序列，每一次选取都是基于原序列。
"""

"""7. random.shuffle(x[,random])：用于将一个列表中的元素打乱，随机排序"""
list99=[random.randint(4, 582) for i in range(4)]
print(list99)
random.shuffle(list99)
print(list99)

"""8. random.sample(sequence,k)：用于从指定序列中随机获取指定长度的片段，sample()函数不会修改原有序列。"""
