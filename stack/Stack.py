
#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :    HY
@Software:   PyCharm
@File    :   Stack.py
@Time    :   2019/7/31 12:51
@Desc    :

'''


class Stack(object):
    """栈"""
    """先进后出"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断是否为空"""
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return  self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    stack=Stack()
    stack.push('huangyang')
    stack.push(1)
    stack.push(2)
    stack.push('adfalfja')
    print(stack.size())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.size())
