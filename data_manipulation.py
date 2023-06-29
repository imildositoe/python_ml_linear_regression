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

    for row in train_data.itertuples():
        print(row[1])
        

        for j in ideal_data.index: # to remove this loop
            pass
            # Calculate the sum of squared deviations for each of the 50 ideal functions using the training datasets.
            # Select the four ideal functions with the lowest sum of squared deviations.
    
    # Return the four selected ideal functions





def main():
    # print(get_data("datasets/train.csv"))
    # print(get_data("datasets/test.csv"))
    # print(get_data("datasets/ideal.csv"))
    squared_deviations()

if __name__ == "__main__":
    main()