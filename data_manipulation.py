"""
@author: Imildo Sitoe
@email: imildo.sitoe@iu-study.org
@description: this file aims to
"""



# Imports
import pandas as pd



"""
Read the training datasets (A), test dataset (B), and ideal functions dataset (C) from the CSV files.
"""
def readFiles():
    data = pd.read_csv("datasets/train.csv")
    print(data)


def main():
    readFiles()

if __name__ == "__main__":
    main()