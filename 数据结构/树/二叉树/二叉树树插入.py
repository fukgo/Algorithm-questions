import random
from collections import deque
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None
class Bit:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.root = self.insert(self.root, val)
                #self.insert(val)

    def insert(self, node, val):
        if not node:  # if not node:  作用等于  if node==None:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        else:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node
    # recursion递归,这里不使用递归
    def insert_no_rec(self, val):
        p = self.root
        while True:
            if not p:
                self.root = BiTreeNode(val)
                return
            if val < p.data:
                if p.lchild:
                    p=p.lchild
                else:
                    p.lchild=BiTreeNode(val)
                    p.lchild.parent = p
                    break
            if val > p.data:
                if p.lchild:
                    p=p.lchild
                else:
                    p.rchild=BiTreeNode(val)
                    p.rchild.parent = p
                    break
                # 等于
            else:
                break
    def pre_order(self,root):
        if root:
            print(root.data, end=" ")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)
    #pre_order(root)
    """2 中序遍历"""
    def in_order(self,root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=" ")
            self.in_order(root.rchild)
    #in_order(root)
    """3 后序遍历"""
    def post_order(self,root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=" ")
    #post_order(root)
    """4 层次遍历"""
    def level_order(self, root):
        queue = deque()
        queue.append(root)
        while len(queue) > 0:       # 只要队不空
            node = queue.popleft()  # 队首出队
            print(node.data, end=" ")
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

li = list(range(1000))
print(li)
random.shuffle(li)
tree=Bit(li)
tree.pre_order(tree.root)
print("---------")
tree.in_order(tree.root)
print("---------")
tree.post_order(tree.root)
print("---------")
tree.level_order(tree.root)





