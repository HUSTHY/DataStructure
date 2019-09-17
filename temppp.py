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

select * from patent where patentId IN (select patentId from patent where isValid=1 AND checkStatus in ("有效", "无效", "待定") AND companyId in (SELECT companyId from confParkCompany where  env="prod" and parkName="华中科技大学科技园创新基地" and isValid=1))