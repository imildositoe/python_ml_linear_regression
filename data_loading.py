'''
@author: Imildo Sitoe <imildo.sitoe@iu-study.org>
@description: this file contains the methods responsible for loading data from the csv files into local dataframes
'''

from sqlalchemy.orm import sessionmaker
import database as db
import pandas as pd

# Creating a session for accessing the database
Session = sessionmaker(bind=db.engine)
session = Session()

# Loading data from csv files into the db created tables
train_list = pd.read_csv('train.csv')
ideal_list = pd.read_csv('ideal.csv')
test_list = pd.read_csv('test.csv')

class DataLoading:
    '''Main class of the Data Loading file containing all the loading methods into the db'''
    def __init__(self):
        pass

    def __loadTrain():
        '''Private method responsible for loading the Train data from the csv into a created dataframe'''
        for row in range(len(train_list)):
            record = db.Train(train_list.loc[row, "x"], train_list.loc[row, "y1"], train_list.loc[row, "y2"], train_list.loc[row, "y3"], train_list.loc[row, "y4"])
            session.add(record)

    def __loadIdeal():
        '''Private method responsible for loading the Ideal data from the csv into a created dataframe'''
        for row in range(len(ideal_list)):
            record = db.Ideal(
                      ideal_list.loc[row, "x"], ideal_list.loc[row, "y1"], ideal_list.loc[row, "y2"], ideal_list.loc[row, "y3"], ideal_list.loc[row, "y4"],
                      ideal_list.loc[row, "y5"], ideal_list.loc[row, "y6"], ideal_list.loc[row, "y7"], ideal_list.loc[row, "y8"], ideal_list.loc[row, "y9"],
                      ideal_list.loc[row, "y10"], ideal_list.loc[row, "y11"], ideal_list.loc[row, "y12"], ideal_list.loc[row, "y13"], ideal_list.loc[row, "y14"],
                      ideal_list.loc[row, "y15"], ideal_list.loc[row, "y16"], ideal_list.loc[row, "y17"], ideal_list.loc[row, "y18"], ideal_list.loc[row, "y19"],
                      ideal_list.loc[row, "y20"], ideal_list.loc[row, "y21"], ideal_list.loc[row, "y22"], ideal_list.loc[row, "y23"], ideal_list.loc[row, "y24"],
                      ideal_list.loc[row, "y25"], ideal_list.loc[row, "y26"], ideal_list.loc[row, "y27"], ideal_list.loc[row, "y28"], ideal_list.loc[row, "y29"],
                      ideal_list.loc[row, "y30"], ideal_list.loc[row, "y31"], ideal_list.loc[row, "y32"], ideal_list.loc[row, "y33"], ideal_list.loc[row, "y34"],
                      ideal_list.loc[row, "y35"], ideal_list.loc[row, "y36"], ideal_list.loc[row, "y37"], ideal_list.loc[row, "y38"], ideal_list.loc[row, "y39"],
                      ideal_list.loc[row, "y40"], ideal_list.loc[row, "y41"], ideal_list.loc[row, "y42"], ideal_list.loc[row, "y43"], ideal_list.loc[row, "y44"],
                      ideal_list.loc[row, "y45"], ideal_list.loc[row, "y46"], ideal_list.loc[row, "y47"], ideal_list.loc[row, "y48"], ideal_list.loc[row, "y49"],
                      ideal_list.loc[row, "y50"]
            )
            session.add(record)

    def __loadTest():
        '''Private method responsible for loading the Test data from the csv into a created dataframe.'''
        for row in range(len(test_list)):
            record = db.Test(test_list.loc[row, "x"], test_list.loc[row, "y"], 0, 0)
            session.add(record)

    def loadDeviations(delta_y, nr_ideal_function):
        '''Public method responsible for saving the deviations and nr_ideal_functions into the db by updating the Test table. 
        This method is public and possible to be called outside'''
        for row in range(len(test_list)):
            session.query(db.Test).filter(db.Test.id == row + 1).\
            update({db.Test.delta_y: delta_y[row], db.Test.nr_ideal_function: nr_ideal_function[row]}, synchronize_session=False)
            session.commit()

    def loadChangesDB():
        '''Public method responsible for calling the 2 independent dataloading functions and commiting the changes into the db.
        This method is public and possible to be called outside and this will be responsible for calling other 2 inner private methods (_loadTrain(), _loadIdeal()).'''
        DataLoading.__loadTrain()
        DataLoading.__loadIdeal()
        DataLoading.__loadTest()
        session.commit()