import random
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

    def query(self, node, val):
        if not node:
            return None
        if node.data<val:
            return self.query(node.rchild, val)
        elif node.data>val:
            return self.query(node.lchild, val)
        #  等于：
        else:
            return node.data

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data<val:
                p = p.rchild
            elif p.data>val:
                p = p.lchild
            else:
                return p
        return None

li = list(range(0, 1000, 2))
random.shuffle(li)
tree=Bit(li)
print(tree.query(tree.root,5))
print(tree.query_no_rec(5))





