"""栈的实现"""
#1
'''push（进栈）'''
'''pop（出栈）'''
'''get top（取栈顶）'''
'''destroy stack（栈销毁）'''
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def get_top(self):
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None
    def is_empty(self):
        return len(self.stack) == 0
    def destroy_stack(self):
        self.stack.clear()


def brace_match(string_list):
    match_dir={'}':'{', ')':'(', ']':'['}
    stack=Stack()
    for i in string_list:
        if i in {'[','(','{'}:
            stack.push(i)
        else:
            if stack.is_empty():
                return False
            elif match_dir[i] == stack.get_top():
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False
stack=Stack()
stack.push(58)
stack.push(45)
stack.push(4)
stack.push(45)
stack.destroy_stack()
print(stack.stack)
print(brace_match('{[[()]]}'))