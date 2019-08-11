#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :    HY
@Software:   PyCharm
@File    :   HuffmanTree.py
@Time    :   2019/8/4 15:51
@Desc    :

'''
class Node(object):
    def __init__(self,name,value):
        self._name=name
        self._value=value
        self._left=None
        self._right=None


class HuffmanTree(object):
    def __init__(self,char_weights):
        self.a=[Node(ele[0],ele[1]) for ele in char_weights ]
        while len(self.a)!=1:
            self.a.sort(key=lambda node:node._value,reverse=True)
            c=Node(name=None,value=self.a[-1]._value+self.a[-2]._value)
            c._left=self.a.pop(-1)
            c._right=self.a.pop(-1)
            self.a.append(c)
        self.root = self.a[0]

    def pre(self,tree,length,l):
        if l==0:
            self.b=[0]*length
        node =tree
        if not node:
            return
        else:
            if node._name is not None:
                print(node._name + '的编码为:', end=' ')
                for i in range(l):
                    print(self.b[i],end='')
                print('\n')
                return

        self.b[l]=0
        self.pre(node._left,length,l+1)
        self.b[l]=1
        self.pre(node._right,length,l+1)

if __name__ == '__main__':
    char_weights = [('a', 9), ('b', 12), ('c', 6), ('d', 3), ('e', 5), ('f', 15)]
    tree = HuffmanTree(char_weights)
    length = len(char_weights)
    tree.pre(tree.root,length,0)