"""
@author: Imildo Sitoe
@email: imildo.sitoe@iu-study.org
@description: this file contains all python assignment task code using oop
"""

import numpy as np
import pandas as pd
import sqlite3

class Connection():

    # Connect to DB and create a cursor
    def database():
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


class Data():
    def dataPreparation():
        x = ''