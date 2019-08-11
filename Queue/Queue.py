#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :    HY
@Software:   PyCharm
@File    :   Queue.py
@Time    :   2019/7/31 13:02
@Desc    :

'''
class Queue(object):
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.size())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.size())