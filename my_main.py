"""
@author: Imildo Sitoe
@email: imildo.sitoe@iu-study.org
@description: this file contains all python assignment task code using oop
"""

import numpy as np
import pandas as pd
import sqlite3

class Connection:
    """This class serves to establish all necessary connections of the application into the database SQLite"""

    def ___init___(self, x1, y1, y2):
        self.x1 = x1
        self.y1 = y1
        self.y2 = y2

    # Connect to DB and create a cursor
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Write a query and execute it with cursor
    cursor.execute('''CREATE TABLE IF NOT EXISTS data (x, y1, y2)''')
    conn.commit()

    # Test data and insert into a database
    function_list = [
        (1, 2, 3),
        (3, 2, 1),
        (2, 1, 3)
    ]
    cursor.executemany('''INSERT INTO data (x, y1, y2) VALUES (?, ?, ?)''', function_list)
    conn.commit()

    # Pull and display data
    function_data = cursor.execute("SELECT * FROM data")
    for row in function_data:
        print(row)

    # Close DB objects
    cursor.close()
    conn.close()


class DataManipulation:
    """DataManipulation class serves to load and manipulate the given .csv files"""

    # Load data
    train = pd.read_csv('datasets/train.csv')
    test = pd.read_csv('datasets/test.csv')
    ideal = pd.read_csv('datasets/ideal.csv')

    def dataPreparation():
        x = ''