#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :    HY
@Software:   PyCharm
@File    :   temppp.py
@Time    :   2019/9/16 14:21
@Desc    :

'''
# SELECT * FROM patent_college WHERE companyId='30bce2146c815640920c8af5b78edf39' AND companyName='华中科技大学'

SELECT patentId,patentName FROM patent_college WHERE isValid=1 AND companyId IN ('30bce2146c815640920c8af5b78edf39','edb1d57ad7106de0708b485dc134ae3a')