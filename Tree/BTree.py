#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :    HY
@Software:   PyCharm
@File    :   BTree.py
@Time    :   2019/8/4 15:20
@Desc    :

'''
class Node(object):
    def __init__(self,item):
        self.elem=item
        self.leftChild=None
        self.rightChild=None

class BTree(object):
    def __init__(self,node=None):
        self.root=node

    def add(self,item):
        node=Node(item)
        if self.root==None:
            self.root=node
        else:
            queue=[]
            queue.append(self.root)
            while queue:
                cur_node=queue.pop(0)
                if cur_node.leftChild is None:
                    cur_node.leftChild=node
                    return
                else:
                    queue.append(cur_node.leftChild)

                if cur_node.rightChild is None:
                    cur_node.rightChild=node
                    return
                else:
                    queue.append(cur_node.rightChild)

    def pre_travel(self,root):
        if root is None:
            return
        else:
            print(root.elem,end=" ")
            self.pre_travel(root.leftChild)
            self.pre_travel(root.rightChild)
    def mid_travel(self,root):
        if root is None:
            return
        else:
            self.mid_travel(root.leftChild)
            print(root.elem, end=" ")
            self.mid_travel(root.rightChild)

    def post_travel(self,root):
        if root is None:
            return
        else:
            self.post_travel(root.leftChild)
            self.post_travel(root.rightChild)
            print(root.elem, end=" ")


    def width_travel(self,root):
        if root is None:
            return
        else:
            queue=[root]
            while queue:
                cur=queue.pop()
                print(cur.elem,end=" ")
                if cur.leftChild is not None:
                    queue.append(cur.leftChild)
                if cur.rightChild is not None:
                    queue.append(cur.rightChild)

if __name__ == '__main__':
    Btree=BTree()
    Btree.add('A')
    Btree.add('B')
    Btree.add('C')
    Btree.add('D')
    Btree.add('E')
    Btree.add('F')
    Btree.add('G')
    Btree.add('H')

    root=Btree.root
    Btree.pre_travel(root)
    print()
    Btree.mid_travel(root)
    print()
    Btree.post_travel(root)
    print()
    Btree.width_travel(root)



