# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:49:49 2019

@author: rhysa
"""
from PIL import Image, ImageDraw, ImageFont
#205, 22
def imgfixxer(date):
       img = Image.open("C:/Users/rhysa/Desktop/CaptureROTCDoc.png")
       draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
       font = ImageFont.truetype("times.ttf", 17)
# draw.text((x, y),"Sample Text",(r,g,b))
       draw.text((200, 16), date, (0,0,0), font = font)
       img.save('C:/Users/rhysa/Desktop/signwdate.png')
imgfixxer('April 12, 2020')


#truetype("/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman.ttf", 12)