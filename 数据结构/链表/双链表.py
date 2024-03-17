"""
双链表的每个节点有两个指针

"""
"""
插入
p.next=curNode.next
curNode.next.prior=p
p.prior=curNode
curNode.next=p

删除
p=curNode.next
curNode.next=p.next
p.next.prior=curNode
del p
"""
class
