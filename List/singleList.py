#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :    HY
@Software:   PyCharm
@File    :   sigleList.py
@Time    :   2019/7/31 11:18
@Desc    :

'''
class SingleNode(object):
    """单链表的结点"""
    def __init__(self, item):
        #  _item存放数据元素
        self.item = item
        #  _next是下一个节点的标识
        self.next = None

class singleLinkList(object):

    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head is None

    def length(self):
        cur = self.head
        count =0
        while cur is not None:
            count+=1
            cur=cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.head
        while cur is not None:
            print(cur.item)
            cur = cur.next
        print()

    def add(self,item):
        """头部添加元素"""
        # 先创建一个保存item节点的值
        node = SingleNode(item)

        node.next=self.head

        self.head=node

    def append(self,item):
        node=SingleNode(item)

        if self.isEmpty():
            self.head=None
        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=node

    def insert(self, index, item):

        if index<=0:
            self.add(item)
        elif index>=(self.length()-1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre =self.head

            while count< index-1:
                count+=1
                pre=pre.next

            node.next=pre.next
            pre.next=node

    def remove(self, item):
        cur=self.head
        pre=None

        while cur is not None:
            if cur.item==item:
                if pre is None:
                    self.head=cur.next
                    cur=None
                else:
                    pre.next=cur.next
                    cur=None
            else:
                pre=cur
                cur=cur.next

if __name__ == '__main__':
    sL=singleLinkList()
    sL.add(5)
    sL.append('huagnyagn')
    sL.insert(1, 8889)
    sL.remove('huagnyagn')
    sL.travel()

    print(sL.length())
