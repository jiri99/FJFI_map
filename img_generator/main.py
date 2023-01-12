# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:59:52 2022

@author: jiri.nabelek
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import yaml

config_path = "./config.yaml"

with open(config_path) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

for building in list(data.keys()):
    for floor in list(data[building].keys()):
        # print(data[building][floor]["path"])
        data[building][floor]["img"] = Image.open(data[building][floor]["path"], "r")

# path = "./images/brehova/patro_1.png"

# # im = Image.open(path, "r") 

# # Read the original image
# img = cv2.imread(path) 
# # Display original image
# cv2.imshow('Original', img)
# cv2.waitKey(0)
 
# # Convert to graycsale
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # Blur the image for better edge detection
# img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
 
# # Sobel Edge Detection
# sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
# sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
# sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# # Display Sobel Edge Detection Images
# cv2.imshow('Sobel X', sobelx)
# cv2.waitKey(0)
# cv2.imshow('Sobel Y', sobely)
# cv2.waitKey(0)
# cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
# cv2.waitKey(0)
 
# # Canny Edge Detection
# edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# # Display Canny Edge Detection Image
# cv2.imshow('Canny Edge Detection', edges)
# cv2.waitKey(0)
 
# cv2.destroyAllWindows()
    
