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

# SUMMARY DATA
# Generate summary data for the numerical variables.
# print(iris.describe())

# Assign a variable to the summary dataframe.
summary = iris.describe() 

# Export the summary dataframe as a txt file
summary.to_string('summary.txt')

# HISTOGRAMS
# Assign variables to each of the dataset measurement variables
sepal_l = iris['sepal_length_cm']
sepal_w = iris['sepal_width_cm']
petal_l = iris['petal_length_cm']
petal_w = iris['petal_width_cm']

# Use matplotlib to plot and style the figure that will house the histogram axes
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(13, 10))
plt.style.use('ggplot')
plt.subplots_adjust(hspace=.3)

# Generate, format, and title the histogram axes for each measurement variable
axes[0, 0].hist(sepal_l, edgecolor='white', bins=15)
axes[0, 0].set_title('Sepal Length Distribution', fontsize=10)
axes[0, 0].set_xlabel('cm', fontsize=10)

axes[0, 1].hist(sepal_w, edgecolor='white', bins=15)
axes[0, 1].set_title('Sepal Width Distribution', fontsize=10)
axes[0, 1].set_xlabel('cm', fontsize=10)

axes[1, 0].hist(petal_l, edgecolor='white', bins=15)
axes[1, 0].set_title('Petal Length Distribution', fontsize=10)
axes[1, 0].set_xlabel('cm', fontsize=10)

axes[1, 1].hist(petal_w, edgecolor='white', bins=15)
axes[1, 1].set_title('Petal Width Distribution', fontsize=10)
axes[1, 1].set_xlabel('cm', fontsize=10)

# Generate a title for the overall figure
fig.suptitle('Distributions of Measurement Variables', fontsize=13)

# Save a copy of the histograms as a png file
plt.savefig('histogram.png')




