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

def insertVaribleIntoTable(id, floor, room_type, name, description, area, image):
    try:
        sqliteConnection = sqlite3.connect('./../db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO DEVELOP
                          (id, floor, room_type, name, description, area, image) 
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""

        data_tuple = (id, floor, room_type, name, description, area, image)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

insertVaribleIntoTable(20, '1', '1', 'Pokus', "", "200,200", "./images/brehova/suterén2.jpg")