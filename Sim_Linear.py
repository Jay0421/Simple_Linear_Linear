
# Import packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset and Describe the data

data = pd.read_csv("tvmarketing.csv")
data.head()

data.info()
data.describe()