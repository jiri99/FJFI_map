# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:59:52 2022

@author: jiri.nabelek
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image, ImageColor
import cv2
import yaml

img_output_path = "./../develop/db_images"
config_path = "./config.yaml"

def display(img):
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.show()

def prerocess_cordinates(cordinates):
    cord_str = cordinates.split(",")
    cord_all = [int(n) for n in cord_str]
    cord = np.zeros([int(len(cord_all)/2),2], dtype=int)
    for i in range(0, len(cord_all), 2):
        cord[int(i/2),:] = cord_all[i:(i+2)]
    return cord
    
def shadow_area(image_floor, room_data):    
    mask = np.zeros(image_floor.shape, dtype=image_floor.dtype)
    cordinates = prerocess_cordinates(room_data["cordinates"])
    cv2.fillConvexPoly(mask, cordinates, 128)
    
    mask_bool = mask > 0
    im = np.zeros_like(image_floor)
    for i in range(image_floor.shape[0]):
        for j in range(image_floor.shape[1]):
            if(mask_bool[i,j] == True and image_floor[i,j] > 128):
                im[i,j] = 128
            else:
                im[i,j] = image_floor[i,j]
    img = Image.fromarray(im)
    return img

def cropp(img, cordinates, x_size = 300, y_size = 300):
    x_middle = np.mean(cordinates[:,0])
    y_middle = np.mean(cordinates[:,1])
    
    cropped_img = img.crop((x_middle-x_size, y_middle-y_size, x_middle+x_size, y_middle+y_size))
    
    plt.imshow(cropped_img, cmap='gray', vmin=0, vmax=255)
    plt.show()

    

with open(config_path) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

for building in list(data.keys()):
    for floor in list(data[building].keys()):
        # print(data[building][floor]["path"])
        # data[building][floor]["img"] = np.array(Image.open(data[building][floor]["path"]))
        data[building][floor]["img"] = cv2.imread(data[building][floor]["path"],0)
        

image_floor = data["Brehova"]["1.patro"]["img"]
# image_floor = cv2.cvtColor(data["Brehova"]["1.patro"]["img"], cv2.COLOR_BGR2RGB)
room_name = "B-101"
room_data = data["Brehova"]["1.patro"]["classes"][room_name]

# %%

# cv2.imshow('Extracted Image', image_floor)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

mask = np.zeros(image_floor.shape, dtype=image_floor.dtype)

cordinates = prerocess_cordinates(room_data["cordinates"])

cv2.fillConvexPoly(mask, cordinates, 128)
# cv2.fillConvexPoly(mask, cordinates, (128,128,128,255))

mask_bool = mask > 0

im = np.zeros_like(image_floor)

for i in range(image_floor.shape[0]):
    for j in range(image_floor.shape[1]):
        if(mask_bool[i,j] == True and image_floor[i,j] > 128):
        # if(mask_bool[i,j,0] == True and image_floor[i,j,0] == 255):
            im[i,j] = 128
            # im[i,j,:] = [255,255,255,1]
        else:
            im[i,j] = image_floor[i,j]
            # im[i,j,:] = image_floor[i,j,:]

# cv2.imshow('Extracted Image', im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img = Image.fromarray(im)

plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()

img.save("pokus.jpg")

#%%
# spočítat průmměr souřadnic a udělat zoom!!!

x_size = 300
y_size = 350

x_middle = np.mean(cordinates[:,0])
y_middle = np.mean(cordinates[:,1])

cropped_img = img.crop((x_middle-x_size, y_middle-y_size, x_middle+x_size, y_middle+y_size))

plt.imshow(cropped_img, cmap='gray', vmin=0, vmax=255)
plt.show()


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
    
