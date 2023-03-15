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
from fill_database import insert_into_database_room, insert_into_database_roomtype
from img_generator import generate_image

img_output_path = "./../develop/db_images/"
config_path = "./config.yaml"
config_path_out = "./config_out.yaml"
id_counter = 18

with open(config_path) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

for building in list(data.keys()):
    for floor in list(data[building].keys()):
        data[building][floor]["img"] = cv2.imread(data[building][floor]["path"],0)
        
for building in list(data.keys()):
    for floor in list(data[building].keys()):
        for room in list(data[building][floor]["classes"].keys()):
            if(not data[building][floor]["classes"][room]["cordinates"] == ""):
                if(data[building][floor]["classes"][room]["saved"] == 0):
                    generate_image(data[building][floor]["img"], data[building][floor]["classes"][room], room, img_output_path)
                    insert_into_database_room(id_counter, data[building][floor]["classes"][room]["name"], "", 1, img_output_path + room + ".jpg", data[building][floor]["classes"][room]["cordinates"])
                    if(data[building][floor]["classes"][room]["type"] == "class"):
                        insert_into_database_roomtype(id_counter, id_counter, 2)
                    elif(data[building][floor]["classes"][room]["type"] == "important"):
                        insert_into_database_roomtype(id_counter, id_counter, 4)
                    elif(data[building][floor]["classes"][room]["type"] == "wc"):
                        insert_into_database_roomtype(id_counter, id_counter, 5)
                    else:
                        insert_into_database_roomtype(id_counter, id_counter, 6)    
                    data[building][floor]["classes"][room]["saved"] = 1
                    id_counter += 1
                    with open(config_path_out, "w") as file:
                        documents = yaml.dump(data, file)
                else:
                    continue
            else:
                continue


