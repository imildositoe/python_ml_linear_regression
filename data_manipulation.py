"""
@author: Imildo Sitoe
@email: imildo.sitoe@iu-study.org
@description: this file aims to
"""


# import numpy as np 
# import pandas as pd 
# import matplotlib.pyplot as plt 
# import seaborn as sns 
# from sklearn.linear_model import Ridge 
# from sklearn.preprocessing import StandardScaler 
# # Load the data 
# train_df = pd.read_csv('datasets/train.csv') 
# test_df = pd.read_csv('datasets/test.csv') 
# ideal_df = pd.read_csv('datasets/ideal.csv') 
# train_df=pd.read_csv('datasets/train.csv') 
# test_df=pd.read_csv('datasets/test.csv')
# ideal_df=pd.read_csv('datasets/ideal.csv') 
# train_df 
# ideal_df 
# test_df 
# plt.figure(figsize=(15,6)) 
# sns.lineplot(x=train_df['x'],y=train_df['y1'],data=train_df) 
# plt.show() 
# plt.figure(figsize=(15,6)) 
# sns.lineplot(x=test_df['x'],y=test_df['y'],data=test_df) 
# plt.show() 
# # Define the features and target 
# X_train = train_df[['x']] 
# y_train = train_df['y1'] 
# X_test = test_df[['x']] 
# y_test = test_df['y'] 
# # Scale the features 
# scaler = StandardScaler() 
# X_train_scaled = scaler.fit_transform(X_train) 
# X_test_scaled = scaler.transform(X_test) 
# # Fit the ridge regression model 
# ridge = Ridge(alpha=1) # Choose a value for alpha 
# ridge.fit(X_train_scaled, y_train) 
# # Predict the target values for the test set 
# y_pred = ridge.predict(X_test_scaled) 
# # Plot the results 
# plt.figure(figsize=(15,6)) 
# sns.lineplot(x=train_df['x'], y=train_df['y1'], data=train_df) 
# sns.lineplot(x=test_df['x'], y=y_pred, color='red') 
# plt.show()
