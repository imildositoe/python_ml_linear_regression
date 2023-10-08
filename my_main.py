"""
@author: Imildo Sitoe
@email: imildo.sitoe@iu-study.org
@description: this file contains all python assignment task code using oop
"""

import numpy as np
import pandas as pd
import sqlalchemy as db

def connection():
    """This function serves to establish all necessary connections of the application into the database SQLite"""

    def ___init___(self, x1):
        self.x1 = x1

    # Create, connect to DB and create the metadata
    eng = db.create_engine('sqlite:///train_db.db')
    conn = eng.connect()
    meta = db.MetaData()

    # Create a table train with all fields
    train = db.Table('train', meta,
                    db.Column('x (training func)', db.Float()),
                    db.Column('y1 (training func)', db.Float()),
                    db.Column('y2 (training func)', db.Float()),
                    db.Column('y3 (training func)', db.Float()),
                    db.Column('y4 (training func)', db.Float()))

    ### Try to load csv data directly and create the  table /// OR /// LOAD THE CSV AND LOOP THE DATA AND EXECUTE QUERIES INSERT INTO THE TRAIN DATA


def dataManipulation():
    """DataManipulation function serves to load and manipulate the given .csv files"""

    # Load data
    train = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')
    ideal = pd.read_csv('ideal.csv')
    print('Start')
    for i in range(len(train)):
        print(train.loc[i, "x"], ' || ', train.loc[i, "y1"])
    

def main():
    dataManipulation()

if __name__ == "__main__":
    main()