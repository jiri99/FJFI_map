# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 20:02:26 2023

@author: jiri.nabelek
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import yaml
import sqlite3

def insert_into_database(id, name, description, floor_id, image, area):
    try:
        sqliteConnection = sqlite3.connect('./../db.sqlite3')
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO develop_room
                          (id, name, description, floor_id, image, area) 
                          VALUES (?, ?, ?, ?, ?, ?);"""

        data_tuple = (id, name, description, floor_id, image, area)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print(name + " inserted successfully into database")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")

insert_into_database(20, "Pokus", "Script test", 1, "images/brehova/suterén2.jpg", "200,200")