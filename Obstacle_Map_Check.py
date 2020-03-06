# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 04:27:01 2020

@author: Arun
"""

import numpy as np
import cv2


def circle(x,y):
    
    if ((np.square(x-225))+ (np.square(y-50)) <=np.square(25)):
        return True
    else:
        return False


def ellipse(x,y):
    
    if (((np.square(x-150))/np.square(40))+((np.square(y-100))/np.square(20)) -1 <=0):
        return True
    else:
        return False
    
def rectangle(x,y):
    
    if (200-y) - (1.73)*x + 135 > 0 and (200-y) + (0.58)*x - 96.35  <= 0 and (200-y) - (1.73)*x - 15.54 <= 0 and (200-y) + (0.58)*x - 84.81 >= 0:
        return True
    else:
        return False

def rhombus(x,y):
    if ((x*(-3/5)+y-55<0) and (x*(3/5)+y-325<0) and (x*(-3/5)+y-25>0) and (x*(3/5)+y-295 > 0)):
        return True
    else:
        return False
    
def polygon1(x,y):
    if((y+13*x-340>0) and x+y-100<0 and y+(-7/5)*x+20>0):
        return True
    else:
        return False

def polygon2(x,y):
    if y-15>0 and (7/5)*x+y-120<0 and y+(-7/5)*x+20<0:
        return True
    else:
        return False

def polygon3(x,y):#rhombus
    if (7/5)*x+y-120>0 and (-6/5)*x+y+10<0 and (6/5)*x+y-170<0 and (-7/5)*x+y+90>0:
        return True
    else:
        return False
    
height = 200
width = 300

image = (np.full([height,width], 0, dtype='uint8'))

for i in range(200):
    for j in range(300):
         if circle(j,i) or ellipse(j,i) or rectangle(j,i) or rhombus(j,i) or polygon1(j,i) or polygon2(j,i) or polygon3(j,i) :
#        if rhombus(j,i):
            image[i][j] = 255
pic=cv2.resize(image,None,fx=3,fy=3)
cv2.imshow("Map",pic)
cv2.waitKey(0)
# cleanup the camera and close any open windows
cv2.destroyAllWindows()