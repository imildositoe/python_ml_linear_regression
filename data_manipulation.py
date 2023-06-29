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






def main():
    print(get_data("datasets/train.csv"))
    print(get_data("datasets/test.csv"))
    print(get_data("datasets/ideal.csv"))

if __name__ == "__main__":
    main()