"""
@author: Imildo Sitoe
@email: imildo.sitoe@iu-study.org
@description: this file aims to
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import unittest

# Step 1: Data Preprocessing
# Read data from CSV files into pandas DataFrames
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
ideal_df = pd.read_csv('ideal.csv')

# Extract x and y columns from the DataFrames
x_train = train_df['x'].values
y_train = train_df[['y1', 'y2', 'y3', 'y4']].values
x_test = test_df['x'].values
y_test = test_df['y'].values
ideal_x = ideal_df['x'].values
ideal_y = ideal_df[['y1', 'y2', 'y3', 'y4']].values

# Step 2: Choose Ideal Functions
# Calculate the sum of squared y-deviations for each ideal function for the training data
def sum_squared_deviations(y_actual, y_ideal):
    return np.sum((y_actual - y_ideal) ** 2, axis=0)

ideal_function_errors = sum_squared_deviations(y_train, ideal_y)

# Select the four ideal functions that minimize the sum of squared deviations
chosen_ideal_indices = np.argsort(ideal_function_errors)[:4]
chosen_ideal_functions = ideal_y[:, chosen_ideal_indices]

# Step 3: Mapping and Deviation Calculation
# Define a function to calculate the deviation for an x-y-pair and an ideal function
def calculate_deviation(y_actual, y_ideal):
    return np.sqrt(np.sum((y_actual - y_ideal) ** 2))

# Assign x-y-pairs from the test dataset to the chosen ideal functions
assignments = []
deviations = []

for i in range(len(x_test)):
    x_val = x_test[i]
    y_val = y_test[i]
    
    min_deviation = float('inf')
    assigned_function = None
    
    for j, ideal_function in enumerate(chosen_ideal_functions.T):
        deviation = calculate_deviation(y_val, ideal_function)
        if deviation < min_deviation and deviation <= np.sqrt(2) * np.max(ideal_function_errors[chosen_ideal_indices[j]]):
            min_deviation = deviation
            assigned_function = j
    
    if assigned_function is not None:
        assignments.append(assigned_function)
        deviations.append(min_deviation)
    else:
        assignments.append(None)
        deviations.append(None)

# Step 4: Visualization
# Create plots to visualize the data, assignments, and deviations
# Visualization of Training Data, Chosen Ideal Functions, and Test Data Assignments
# Plot the training data
plt.figure(figsize=(10, 6))
plt.scatter(x_train, y_train[:, 0], label='Training Data y1', marker='o', color='b', alpha=0.5)
plt.scatter(x_train, y_train[:, 1], label='Training Data y2', marker='s', color='g', alpha=0.5)
plt.scatter(x_train, y_train[:, 2], label='Training Data y3', marker='^', color='r', alpha=0.5)
plt.scatter(x_train, y_train[:, 3], label='Training Data y4', marker='*', color='m', alpha=0.5)

# Plot the chosen ideal functions
for i, ideal_function in enumerate(chosen_ideal_functions.T):
    plt.plot(ideal_x, ideal_function, label=f'Chosen Ideal Function {i + 1}', linestyle='--')

# Plot the test data with assignments and deviations
for i, assignment in enumerate(assignments):
    if assignment is not None:
        color = ['b', 'g', 'r', 'm'][assignment]
        plt.scatter(x_test[i], y_test[i], label=f'Test Data {i}', marker='x', color=color)
        plt.annotate(f'Deviation: {deviations[i]:.2f}', (x_test[i], y_test[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Data Visualization')
plt.show()


# Step 5: Unit Tests
# Write unit tests for your functions
class TestCalculateDeviation(unittest.TestCase):
    def test_deviation_calculation(self):
        y_actual = np.array([1.0, 2.0, 3.0])
        y_ideal = np.array([0.5, 2.5, 3.5])
        deviation = calculate_deviation(y_actual, y_ideal)
        self.assertAlmostEqual(deviation, 0.5, delta=1e-6)


# Main program
if __name__ == "__main__":
    # Print the chosen ideal function indices
    print("Chosen Ideal Function Indices:", chosen_ideal_indices)
    
    # Print the assignments and deviations for each test data point
    for i in range(len(x_test)):
        print(f"Test Data ({x_test[i]}, {y_test[i]}):")
        print(f"Assigned Ideal Function: {assignments[i]}")
        print(f"Deviation: {deviations[i]}")
        print("\n")
