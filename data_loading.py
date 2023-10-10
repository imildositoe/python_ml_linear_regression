from sqlalchemy.orm import sessionmaker
import database as db
import pandas as pd

#Creating a session
Session = sessionmaker(bind=db.engine)
session = Session()

# Loading data from csv files into the db created tables
train_list = pd.read_csv('train.csv')
ideal_list = pd.read_csv('ideal.csv')
test_list = pd.read_csv('test.csv')

for row in range(len(train_list)):
    record = db.Train(row + 1, train_list.loc[row, "x"], train_list.loc[row, "y1"], train_list.loc[row, "y2"], train_list.loc[row, "y3"], train_list.loc[row, "y4"])
    session.add(record)

for row in range(len(ideal_list)):
    record = db.Ideal(row + 1, 
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

# Statement to load data into test table
for row in range(len(test_list)):
    record = db.Test(row + 1, test_list.loc[row, "x"], test_list.loc[row, "y"], None, None)
    session.add(record)

# Commiting the changes into the db
session.commit()