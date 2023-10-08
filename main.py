"""
@author: Imildo Sitoe
@email: imildo.sitoe@iu-study.org
@description: this file contains all python assignment task code using oop
"""

from sqlalchemy.orm import sessionmaker
import database as db
import numpy as np
import pandas as pd

#Creating a session
Session = sessionmaker(bind=db.engine)
session = Session()


# Iteration with a filter case
# for row in session.query(db.Train).filter(db.Train.x > 1):
#     print(row)


for row in session.query(db.Train).all():
    print(row.x, row.y1)


########### Youtube how to create a training model || check results of ChatGPT as well ############
