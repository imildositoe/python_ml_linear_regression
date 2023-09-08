"""
@author: Imildo Sitoe
@email: imildo.sitoe@iu-study.org
@description: this file aims to
"""

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('datasets/train.csv')

plt.scatter(data.x, data.y1, data.y2, data.y3, data.y4)
plt.show()