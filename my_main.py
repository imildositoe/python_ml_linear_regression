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
    

    # Write a query and execute it with cursor
    

    # Test data and insert into a database
    

    # Pull and display data
    

    # Close DB objects
    


class DataManipulation:
    """DataManipulation class serves to load and manipulate the given .csv files"""

    # Load data
    train = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')
    ideal = pd.read_csv('ideal.csv')

    print(train[0])

    # Extract data
    