"""
@author: Imildo Sitoe
@email: imildo.sitoe@iu-study.org
@description: this file contains all python assignment task code using oop
"""

import numpy as np
import pandas as pd
import sqlite3

class Connection():
    cursor = ''

    #Connect to DB and create a cursor
    def connect():
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

    # Write a query and execute it with cursor
    query = 'select sqlite_version();'
    cursor.execute(query)


class Data():
    def dataPreparation():
        xx