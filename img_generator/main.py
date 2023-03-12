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
from fill_database import insert_into_database
from img_generator import generate_image

img_output_path = "./../develop/db_images/"
config_path = "./config.yaml"
id_counter = 18

with open(config_path) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

for building in list(data.keys()):
    for floor in list(data[building].keys()):
        data[building][floor]["img"] = cv2.imread(data[building][floor]["path"],0)
        
for building in list(data.keys()):
    for floor in list(data[building].keys()):
        for room in list(data[building][floor]["classes"].keys()):
            generate_image(data[building][floor]["img"], data[building][floor]["classes"][room], room, img_output_path)
            insert_into_database(id_counter, data[building][floor]["classes"][room]["name"], "", 1, img_output_path + room + ".jpg", data[building][floor]["classes"][room]["cordinates"])
            
            id_counter += 1




