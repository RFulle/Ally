# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:34:53 2019

@author: rhysa
"""
'''
, options= {
              "py2exe":{
                            "includes": ["os", "comtypes", "time", "docx", "PyPDF2"]
                            }
              },'''
from distutils.core import setup
import py2exe

setup(console=['PromotionCertificateMaker.py'])