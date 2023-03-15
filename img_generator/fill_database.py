# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 20:02:26 2023

@author: jiri.nabelek
"""
import os, sys
import numpy as np
import math
import matplotlib.pyplot as plt
import yaml
import sqlite3

def insert_into_database_room(id, name, description, floor_id, image, area):
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

def insert_into_database_roomtype(id, id_room, id_type):
    try:
        sqliteConnection = sqlite3.connect('./../db.sqlite3')
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO develop_room_room_type
                          (id, room_id, room_type_id) 
                          VALUES (?, ?, ?);"""

        data_tuple = (id, id_room, id_type)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print(str(id_room) + " inserted successfully into database")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
