#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :    HY
@Software:   PyCharm
@File    :   DoubleList.py
@Time    :   2019/7/31 12:25
@Desc    :

'''
class Node(object):
    def __init__(self,item):
        self.item=item
        self.next=None
        self.pre=None

class DLinkedList(object):
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head is None

    def length(self):
        """返回链表的长度"""
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.head
        while cur is not None:
            print(cur.item)
            cur = cur.next

    def add(self,item):
        node = Node(item)
        if self.head==None:
            self.head=node
        else:
           node.next=self.head
           self.head.pre=node
           self.head=node

    def append(self, item):
        """尾部插入元素"""
        node = Node(item)
        if self.isEmpty():
            # 如果是空链表，将_head指向node
            self.head = node
        else:
            # 移动到链表尾部
            cur = self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=node
            node.pre=cur

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos - 1):
                count += 1
                cur = cur.next

            node.next=cur
            node.pre= cur.pre
            cur.pre.next=node
            cur.pre=node

    def remove(self, item):
        """删除元素"""
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                # 如果首节点的元素即是要删除的元素
                if cur.next == None:
                    # 如果链表只有这一个节点
                    self._head = None
                else:
                    # 将第二个节点的prev设置为None
                    cur.next.prev = None
                    # 将_head指向第二个节点
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    # 将cur的前一个节点的next指向cur的后一个节点
                    cur.prev.next = cur.next
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    cur.next.prev = cur.prev
                    break
                cur = cur.next

if __name__ == '__main__':
    DL=DLinkedList()
    DL.add(1)
    DL.add(2)
    DL.add(3)
    DL.append(4)
    DL.travel()