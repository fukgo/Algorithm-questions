class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child=None
        self.right_child=None
        self.parent = None
class Bst:
    def __init__(self):
        self.root = None
    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lift_child = self.insert(node.left_child, val)
            node.left_child.parent = node
        elif val > node.data:
            node.right_child = self.insert(node.right_child, val)
            node.right_child.parent = node
        return node





#查询
#插入
#删除