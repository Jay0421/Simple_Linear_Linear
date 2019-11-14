
# Import packages

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import seaborn as sn

# Load the dataset and Describe the data

data = pd.read_csv("tvmarketing.csv")
data.head()

data.info()
data.describe()

# Visualize the data

sn.pairplot(data, x_vars=["TV"], y_vars=["Sales"], size = 7, aspect = 0.7, kind = "scatter")

