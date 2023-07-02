"""
@author: Imildo Sitoe
@email: imildo.sitoe@iu-study.org
@description: this file aims to
"""



# Imports
import pandas as pd



"""
Function to read the CSV files
"""
def get_data(file_path):
    return pd.read_csv(file_path)


"""
Function to calculate the squared deviations of the data
"""
def squared_deviations():
    train_data = get_data("datasets/train.csv")
    test_data = get_data("datasets/test.csv")
    ideal_data = get_data("datasets/ideal.csv")


    # Calculate the sum of squared deviations for each of the 50 ideal functions using the training datasets.
    # Select the four ideal functions with the lowest sum of squared deviations.
    for index, row in ideal_data.iterrows():
        for column in ideal_data.columns:
            value = row[column]
            print(value)
            # y1 = (y11 - Y1(x1))^2, (y21 - Y1(x2))^2, ..., (y1n - Y1(xn))^2
            # y1 = sum ((y11 - Y1(x1))^2)) + ((y21 - Y1(x2))^2) + ,..., (y1n - Y1(xn))^2))
            # y2 = sum ((y12 - Y2(x1))^2)) + ((y21 - Y1(x2))^2) + ,..., (y1n - Y1(xn))^2))

            # select the 4 lowest between [y1, y2, ..., yn]
    
    # Return the four selected ideal functions





def main():
    # print(get_data("datasets/train.csv"))
    # print(get_data("datasets/test.csv"))
    # print(get_data("datasets/ideal.csv"))
    squared_deviations()

if __name__ == "__main__":
    main()