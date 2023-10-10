'''
@author: Imildo Sitoe <imildo.sitoe@iu-study.org>
@description: this file contains all python assignment task code using oop
'''

from sqlalchemy.orm import sessionmaker
import database as db
import data_loading as dl
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#Creating a session
Session = sessionmaker(bind=db.engine)
session = Session()

# Iteration with a filter case
# for row in session.query(db.Train).filter(db.Train.x > 1):
#     print(row)

# Normal iteration
# for row in session.query(db.Train).all():
#     print(row.x, row.y1)

# Querying Train data from sqlite database and converting to dataframe
train_data = session.query(db.Train.__table__).all()
df_train = pd.DataFrame(train_data)
x_train = df_train[['x']]
y_train = df_train.drop(columns=['id', 'x'])

# Querying Ideal data from sqlite database and converting to dataframe
ideal_data = session.query(db.Ideal.__table__).all()
df_ideal = pd.DataFrame(ideal_data)
x_ideal = df_ideal[['x']]
y_ideal = df_ideal.drop(columns=['id', 'x'])

# Querying Test data from sqlite database and converting to dataframe
test_data = session.query(db.Test.__table__).all()
df_test = pd.DataFrame(test_data)
x_test = df_test[['x']]
y_test = df_test[['y']]

# Visualizing the original data logically as described in the task
plt.scatter(x_train, y_train[['y1']], color='red')
plt.scatter(x_train, y_train[['y2']], color='green')
plt.scatter(x_train, y_train[['y3']], color='magenta')
plt.scatter(x_train, y_train[['y4']], color='blue')
plt.xlabel('X value')
plt.ylabel('Y value')
plt.title('ORIGINAL DATA')
plt.show()

# Creating a linear regression model and training it
lr = LinearRegression()
lr.fit(x_train, y_train)

# Executing the prediction of x and visualizing logically
y_pred_train = lr.predict(x_train)
plt.scatter(y_train, y_pred_train)
plt.xlabel('Y training')
plt.ylabel('Y prediction training')
plt.title('PREDICTION DATA')
plt.show()

# Checking the score of the prediction
pred_score = r2_score(y_train, y_pred_train)

# Testing the model using the test dataset
y_pred_test = lr.predict(x_test)
# plt.scatter(y_test, y_pred_test)
# plt.xlabel('Y test')
# plt.ylabel('Y prediction test')
# plt.title('TEST DATA')
# plt.show()

# Deviation and Ideal functions section (Choosing the ideal fucntion)
# Return the sum of squared y deviations for each ideal function for the provided training data
def sum_squared_dev(y_train, y_ideal):
    return np.sum((y_train - y_ideal) ** 2, axis=0)

ideal_function_errors = sum_squared_dev(y_train, y_ideal)

# Choosing the 4 ideal functions that minimize the sum of squared deviations
chosen_ideal_indices = np.argsort(ideal_function_errors)[:4]
chosen_ideal_functions = y_ideal[:, chosen_ideal_indices]

# Deviation and Ideal functions section (mapping and calculating the deviation)
# Deviation calculation for x-y pair and ideal function
def get_deviation(y_test, y_ideal):
    return np.sqrt(np.sum((y_test - y_ideal) ** 2))

# Attribute x-y pairs from the test dataset to the chosen ideal functions
deviations = []
assignments = []

for i in range(len(x_test)):
    x_val = x_test[i]
    y_val = y_test[i]

    assigned_function = None
    min_dev = float('inf')
    
    for j, ideal_function in enumerate(chosen_ideal_functions.T):
        deviation = get_deviation(y_val, ideal_function)
        if deviation < min_dev and deviation <= np.sqrt(2) * np.max(ideal_function_errors[chosen_ideal_indices[j]]):
            min_dev = deviation
            assigned_function = j

    if assigned_function is not None:
        assignments.append(assigned_function)
        deviations.append(min_dev)
    else:
        assignments.append(None)
        deviations.append(None)

# Logically visualize the chosen ideal functions
# for i, ideal_function in enumerate(chosen_ideal_functions.T):
#     plt.plot(ideal_x, ideal_function, label=f'Chosen Ideal Function {i + 1}', linestyle='--')

# # Plot the test data with assignments and deviations
# for i, assignment in enumerate(assignments):
#     if assignment is not None:
#         color = ['b', 'g', 'r', 'm'][assignment]
#         plt.scatter(x_test[i], y_test[i], label=f'Test Data {i}', marker='x', color=color)
#         plt.annotate(f'Deviation: {deviations[i]:.2f}', (x_test[i], y_test[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.title('Data Visualization')
# plt.show()

# Showing the assignments and deviations for each test data point
print("Chosen ideal function indices:", chosen_ideal_indices)

for i in range(len(x_test)):
        print(f"Test data ({x_test[i]}, {y_test[i]}):")
        print(f"Assigned ideal function: {assignments[i]}")
        print(f"Deviation: {deviations[i]}")
        print("\n")
        print('#########################################')



def main():
     '''Method to initialize the whole program by calling all necessary methods to load the data, save in the SQLite db, perform the calculations and visualize logically.'''

     # Calling the method to load all data into the database, inclusive the deviations and its assigned functions
     delta_y = pd.DataFrame(deviations)
     nr_ideal_function = pd.DataFrame(deviations)
     dl.DataLoading.loadChangesDB(delta_y, nr_ideal_function)


# Calling the method main to run the program.
if __name__ == 'main':
     main()