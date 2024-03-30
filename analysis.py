# analysis.py
# A project analysing the Iris dataset
# Author: Paul O'Shaughnessy


# Import Libraries to be used for analysis of dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import pairplot

# Import iris dataset. Assign iris as the dataframe name.
iris = pd.read_csv('iris.data')

# Check dataset has loaded
# print(iris.head(5))

# Assign Column titles to dataset
iris.columns = [
                'sepal_length_cm', 
                'sepal_width_cm', 
                'petal_length_cm', 
                'petal_width_cm',
                'class'
                ]     

# Check that Column titles have assigned as expected.
# print(iris.head(5))             

# Generate summary data for the numerical variables.
# print(iris.describe())






