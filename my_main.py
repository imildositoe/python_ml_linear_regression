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

    # Create, connect to DB and create the metadata
    eng = db.create_engine('sqlite:///ml_db.db')
    conn = eng.connect()
    meta = db.MetaData()

    # Create the tables with all fields
    train_table = db.Table('train', meta,
                    db.Column('x', db.Float),
                    db.Column('y1', db.Float),
                    db.Column('y2', db.Float),
                    db.Column('y3', db.Float),
                    db.Column('y4', db.Float))
    meta.create_all(eng)
    
    # test_table = db.Table('test', meta,
    #                 db.Column('x (training func)', db.Float()),
    #                 db.Column('y1 (training func)', db.Float()),
    #                 db.Column('y2 (training func)', db.Float()),
    #                 db.Column('y3 (training func)', db.Float()),
    #                 db.Column('y4 (training func)', db.Float()))
    
    # ideal_table = db.Table('ideal', meta,
    #                 db.Column('x (training func)', db.Float()),
    #                 db.Column('y1 (training func)', db.Float()),
    #                 db.Column('y2 (training func)', db.Float()),
    #                 db.Column('y3 (training func)', db.Float()),
    #                 db.Column('y4 (training func)', db.Float()))


    # Loading data from csv files into the db created tables
    train_list = pd.read_csv('train.csv')
    test_list = pd.read_csv('test.csv')
    ideal_list = pd.read_csv('ideal.csv')

    for row in range(len(train_list)): # inserting train data
        # for column in range(len(train_list.loc[row])):

        # train_query = train_table.insert().values(data)
        # print('x = ', train_list.loc[row, "x"])
        # print('y1 = ', train_list.loc[row, "y1"])
        # print('y2 = ', train_list.loc[row, "y2"])
        # print('y3 = ', train_list.loc[row, "y3"])
        # print('y4 = ', train_list.loc[row, "y4"])
        
        result = conn.execute('INSERT INTO "train" (x, y1, y2, y3) VALUES (train_list.loc[row, "x"], train_list.loc[row, "y1"], train_list.loc[row, "y2"], train_list.loc[row, "y3"], train_list.loc[row, "y4"])')
        # result = conn.execute(train_query)
    print(result)

    # output = conn.execute(db.select([train_table])).fetchall()
    # print(output)

    # print('Row ', row,', column ', column, ':', train_list.loc[row][column])



def dataManipulation():
    """DataManipulation function serves to load and manipulate the given .csv files"""
    

def main():
    connection()

if __name__ == "__main__":
    main()