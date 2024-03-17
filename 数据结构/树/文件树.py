class Node():
    def __init__(self, name, type='dir'):
        self.name = name
        self.parent = None
        self.type = type
        self.children = []

    def __repr__(self):
        return self.name

class FilesystemTree():
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent=self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name[-1] != "/":
            name += "/"
        if name == "../"
            self.now = self.now.parent
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise ValueError("no find file name.")

file = FilesystemTree()
file.mkdir("fir")
file.mkdir("cen")
file.mkdir("third")
print(file.ls())
file.cd("cen/")










