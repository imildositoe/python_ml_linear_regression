"""
@author: Imildo Sitoe
@email: imildo.sitoe@iu-study.org
@description: this file aims to
"""


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.linear_model import Ridge 
from sklearn.preprocessing import StandardScaler 
# Load the data 
train_df = pd.read_csv('datasets/train.csv') 
test_df = pd.read_csv('datasets/test.csv') 
ideal_df = pd.read_csv('datasets/ideal.csv') 
train_df=pd.read_csv('datasets/train.csv') 
test_df=pd.read_csv('datasets/test.csv')
ideal_df=pd.read_csv('datasets/ideal.csv') 
train_df 
ideal_df 
test_df 
plt.figure(figsize=(15,6)) 
sns.lineplot(x=train_df['x'],y=train_df['y1'],data=train_df) 
plt.show() 
plt.figure(figsize=(15,6)) 
sns.lineplot(x=test_df['x'],y=test_df['y'],data=test_df) 
plt.show() 
# Define the features and target 
X_train = train_df[['x']] 
y_train = train_df['y1'] 
X_test = test_df[['x']] 
y_test = test_df['y'] 
# Scale the features 
scaler = StandardScaler() 
X_train_scaled = scaler.fit_transform(X_train) 
X_test_scaled = scaler.transform(X_test) 
# Fit the ridge regression model 
ridge = Ridge(alpha=1) # Choose a value for alpha 
ridge.fit(X_train_scaled, y_train) 
# Predict the target values for the test set 
y_pred = ridge.predict(X_test_scaled) 
# Plot the results 
plt.figure(figsize=(15,6)) 
sns.lineplot(x=train_df['x'], y=train_df['y1'], data=train_df) 
sns.lineplot(x=test_df['x'], y=y_pred, color='red') 
plt.show()

###################################################################################################################

import pandas as pd 
import sqlalchemy as db 
from sqlalchemy import create_engine 
import sqlite3 as sql 
from sklearn import linear_model 
import os 
import matplotlib.pyplot as plt 
import numpy as np 

def regression(test_data, reg): 
    print("Predicted from {} is {}.".format(test_data, reg.predict(test_data))) 

def main(): 
    #Error handling when creating the engine to SQLite 
    try: 
        engine = create_engine('sqlite:///test.db', echo=False) 
    except: 
        print("Failed to create engine.") 
        #Read data from csv file and store it to dataframe 
        train_df = pd.read_csv(os.path.join(os.getcwd(), "train.csv")) 
        #Create new table in SQLite based on dataframe 
        train_df.to_sql('train_table',con=engine, index=False, if_exists='replace') 
        #regress to train the data 
        train_x = np.asanyarray(train_df[['x']]) 
        train_y = np.asanyarray(train_df[['y1']]) 
        global reg 
        reg = linear_model.LinearRegression() 
        reg.fit(train_x, train_y) 
        coef = reg.coef_ 
        intercept = reg.intercept_ 
        print('Coefficient/slope: {}'.format(coef)) 
        print('Intercept: {}'.format(intercept)) 

        #plotting the training data with regression result 
        plt.scatter(train_df.iloc[:,0], train_df.iloc[:,1], color='blue') 
        plt.plot(train_x, coef * train_x + intercept, color='red') 
        plt.xlabel('Train X') 
        plt.ylabel('Train Y')
        plt.show()

        #regression to predict - best candidate for the function 
        test_data = [[8]]
        regression(test_data,reg)

if __name__ == "__main__":
    main()