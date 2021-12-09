# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:10:40 2021

@author: 91872
"""
import time
import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure, color, io
from skimage.feature import peak_local_max
from scipy import ndimage as ndi
import skimage
import os


def size(image):
    image= image[0:400, 50:800]
    #print(filename)
    # cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
     
    hsv= cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_color = np.array([0,69,45]) #9  #binary detection 12/11/2021
    upper_color = np.array([24,251,255])
    
    binary = cv2.inRange(hsv, lower_color, upper_color)
    cv2.imshow('binary', binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #Dis_count=len(contours)
    
    s=0
    m=0
    l=0
    for cnt in contours:
        hull = cv2.convexHull(cnt)
        aaa=cv2.contourArea(hull)
        rect = cv2.minAreaRect(cnt)             # rect = ((center_x,center_y),(width,height),angle)
        l=rect[1][0]
        w=rect[1][1]
        area=l*w
        if l>w:
            length=l
            width=w
        else:
            length=w
            width=l
        area=length*width
        #print('length',length) 
        # print('width',width) 
        # print('area',aaa)
   
        if aaa>3000 and aaa<=48000:
            result='S'
            print('SMALL',round(aaa))
    

            print('area',aaa)
            s+=1
          
        elif aaa>48000 and aaa<56000:
            result='s'
            print('MEDIUM',round(aaa))

         
            m+=1
            print('area',aaa)
            
        elif aaa>=56000 and aaa<66000:

            result='m'
            print('LARGE',round(aaa))

            l+=1    
            print('area',aaa)  
            
        elif aaa>=66000 and aaa<2000000:
             print('LARGE',round(aaa))
             result='l'
            
        else:
            pass
    
    # cv2.imshow('output',image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
          
    
    return result
    

    
folder="C:/Users/91872/Desktop/pomagranate/a grade/200-250gm/Right_Cam"
for filename in os.listdir(folder):
    image = cv2.imread(os.path.join(folder,filename))
    a=size(image)
    print(a)
#image = cv2.imread("E:/Gherkin/1/Cam2/k82.jpg")
    # image = cv2.resize(image, (1000, 1000))