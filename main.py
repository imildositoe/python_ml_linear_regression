"""
@author: Imildo Sitoe
@email: imildo.sitoe@iu-study.org
@description: this file contains all python assignment task code using oop
"""

from sqlalchemy.orm import sessionmaker
import database as db
import data_loading
import numpy as np
import pandas as pd

#Creating a session
Session = sessionmaker(bind=db.engine)
session = Session()
# dl = data_loading


# Iteration with a filter case
# for row in session.query(db.Train).filter(db.Train.x > 1):
#     print(row)


for row in session.query(db.Train).all():
    print(row.x, row.y1)


train_data = session.query(db.Train.__table__).all()
df = pd.DataFrame(train_data)
x = df['x']
y = df.drop(columns=['id', 'x'])

print('-----------------------XXXXXXXXXX------------------------')
print(x)
print('-----------------------YYYYYYYYYY------------------------')
print(y)