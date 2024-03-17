class Linklist:
    class Node:
        def __init__(self, item=None):
            self.item=item
            self.next=None

    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node=self.node
                self.node=cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head=None
        self.tail=None
        if iterable:
            self.extend(iterable)

    #  尾插
    def appened(self, obj):
        s=Linklist.Node(obj)
        if not self.head:
            self.head=s
            self.tail=s
        else:
            self.tail.next=s
            self.tail=s

    def extend(self, iterable):
        for obj in iterable:
            self.appened(obj)


    def find(self, obj):
        for n in self:
            if n == obj:
                return True

    def __iter__(self):
        return self.LinkListIterator(self.head)

    # 打印的时候转换为字符串
    def __repr__(self):
        return "<<"+",".join(map(str, self))+">>"

class HashTable:
    def __init__(self, size=101):
        self.size=size
        self.T = [Linklist() for i in range(size)]

    def h(self, k):
        return k%self.size

    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print("Duplicated Insert.")
        else:
            self.T[i].appened(k)

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)
"""
lk = Linklist([4,5,4,8,5,2,1])
print(lk)"""
ht = HashTable()

ht.insert(4)
ht.insert(1)
#
hs=HashTable()
hs.insert(4)
hs.insert(7)
hs.insert(725)
hs.insert(74)
print(hs.T)


