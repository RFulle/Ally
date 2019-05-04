# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:12:47 2019

@author: rhysa
"""

name = input("enter name")
nummy = name.find(' ')
nummy = nummy
name1 = name[nummy:]
name2 = name[:nummy]
print('{}, {}'.format(name1, name2))