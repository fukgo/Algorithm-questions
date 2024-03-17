"""这一个创建链表的代码，它使用了一个Node类来表示链表的节点。create_linklist_head函数接受一个列表作为参数，然后将列表中的元素逐个添加到链表中。具体的实现是从列表的第一个元素开始，创建一个头节点，然后遍历列表的其他元素，创建新的节点，并将其插入到链表的头部。最后返回链表的头节点。
这两行代码是创建链表节点的部分。

第一行代码创建了链表的头节点，使用列表中的第一个元素作为节点的值。

第二行代码创建了其他节点，使用列表中的其他元素作为节点的值。

这两行代码都使用了Node类来创建节点对象，并将列表中的元素作为参数传递给节点的构造函数，从而创建了具有对应值的节点对象。
"""
class Node:
    def __init__(self,item):
        """"
        这段代码定义了一个名为Node的类。该类有一个构造函数`__init__`，接受一个参数`item`。在构造函数中，将传入的`item`赋值给实例变量`self.item`，并将实例变量`self.next`初始化为None。

这个类表示一个链表的节点，每个节点包含一个数据项`item`和一个指向下一个节点的指针`next`。"""
        self.item=item
        self.next=None
def create_linklist_head(li):
    head=Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next=head
        head=node
    return head

def create_linklist_tail(li):
    head=Node(li[0])
    tail=head
    for element in li[1:]:
        node=Node(element)
        tail.next=node
        tail=node
    return head



def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk=lk.next
lk=create_linklist_tail([1,2,3,4,5,6,7])
print(lk.item)


#链表节点的插入
"""
p.next = curNode.next
cureNode.next=p
"""
#链表节点的删除
"""
p = curNode.next
cureNode.next=cureNode.ext.next
del p
"""
