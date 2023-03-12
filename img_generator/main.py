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

img_output_path = "./../develop/db_images/"
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
    
def shadow_area(image_floor, cordinates):    
    mask = np.zeros(image_floor.shape, dtype=image_floor.dtype)
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
    return cropped_img

def generate_image(image_floor, room_data, room_name, img_output_path):
    cordinates = prerocess_cordinates(room_data["cordinates"])
    img = shadow_area(image_floor, cordinates)
    image = cropp(img, cordinates)
    display(image)
    image.save(img_output_path + room_name + ".jpg")
    

with open(config_path) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

for building in list(data.keys()):
    for floor in list(data[building].keys()):
        # data[building][floor]["img"] = np.array(Image.open(data[building][floor]["path"]))
        data[building][floor]["img"] = cv2.imread(data[building][floor]["path"],0)
        
for building in list(data.keys()):
    for floor in list(data[building].keys()):
        for room in list(data[building][floor]["classes"].keys()):
            generate_image(data[building][floor]["img"], data[building][floor]["classes"][room], room, img_output_path)
            data[building][floor]["classes"][room]["Image"] = img_output_path + room + ".jpg"
            data[building][floor]["classes"][room]["Name"] = room
            data[building][floor]["classes"][room]["Floor"] = floor
            data[building][floor]["classes"][room]["Description"] = ""




