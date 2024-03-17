# all(iterable),如果iterable的所有元素均为Ture（或iterable为空）则返回Ture
#等价于：
def all(iterable):
    for element in iterable:
        if not element:
            return False
        return True