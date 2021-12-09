import time
import cv2
import cv2 as cv
import numpy as np

import os
def color(image):
   
    image= image[80:500, 100:500]
    result ='N'
    image1a=image
    image11=image

    cv2.imshow("crop", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
     
    hsv= cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_color = np.array([0,190,26]) #45  #binary detection 12/11/2021
    upper_color = np.array([3,255,255])#70 
    
    binary = cv2.inRange(hsv, lower_color, upper_color)
    cv2.imshow('binary', binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    aa= cv2.countNonZero(binary)
    print(aa)
    
    if aa>100 and aa<3000:
        result= 'R'
    elif aa>3000 and aa<6000:
        result= 'E'
    elif aa>6000:
        result= 'P'
    else:
        pass
        
    
    return result 

# folder="C:/Users/91872/Desktop/pomagranate/premium/Camera/Right_Cam"
# for filename in os.listdir(folder):
#     image = cv2.imread(os.path.join(folder,filename))
#     a=color(image)
#     print(a)


Image = cv2.imread("C:/Users/91872/Desktop/l65.jpg")
b=color(Image)    