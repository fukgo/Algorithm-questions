"""
前序遍历：根结点 ---> 左子树 ---> 右子树

中序遍历：左子树---> 根结点 ---> 右子树

后序遍历：左子树 ---> 右子树 ---> 根结点

层次遍历：只需按层次遍历即可
"""
from collections import deque
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child=None
        self.right_child=None

a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")
e.left_child=a
e.right_child=g
a.right_child=c
c.left_child=b
c.right_child=d
g.right_child=f
root=e
print(e)
"""1 前序遍历"""
def pre_order(root):
    if root:
        print(root.data, end=" ")
        pre_order(root.left_child)
        pre_order(root.right_child)
#pre_order(root)
"""2 中序遍历"""
def in_order(root):
    if root:
        in_order(root.left_child)
        print(root.data, end=" ")
        in_order(root.right_child)
#in_order(root)
"""3 后序遍历"""
def post_order(root):
    if root:
        post_order(root.left_child)
        post_order(root.right_child)
        print(root.data, end=" ")
#post_order(root)
"""4 层次遍历"""
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:       # 只要队不空
        node = queue.popleft()  # 队首出队
        print(node.data, end=" ")
        if node.left_child:
            queue.append(node.left_child)
        if node.right_child:
            queue.append(node.right_child)
level_order(root)

