# analysis.py
# A project analysing the Iris dataset
# Author: Paul O'Shaughnessy


# Import Libraries to be used for analysis of dataset
import warnings
warnings.simplefilter(action='ignore', category=(FutureWarning, UserWarning))
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
# summary = iris.describe() 

# Export the summary dataframe as a txt file
# summary.to_string('summary.txt')

# HISTOGRAMS
# Assign variables to each of the dataset measurement variables
# sepal_l = iris['sepal_length_cm']
# sepal_w = iris['sepal_width_cm']
# petal_l = iris['petal_length_cm']
# petal_w = iris['petal_width_cm']

# Use matplotlib to plot and style the figure that will house the histogram axes
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(13, 10))
# plt.style.use('ggplot')
# plt.subplots_adjust(hspace=.3)

# Generate, format, and title the histogram axes for each measurement variable
# axes[0, 0].hist(sepal_l, edgecolor='white', bins=15)
# axes[0, 0].set_title('Sepal Length Distribution', fontsize=10)
# axes[0, 0].set_xlabel('cm', fontsize=10)

# axes[0, 1].hist(sepal_w, edgecolor='white', bins=15)
# axes[0, 1].set_title('Sepal Width Distribution', fontsize=10)
# axes[0, 1].set_xlabel('cm', fontsize=10)

# axes[1, 0].hist(petal_l, edgecolor='white', bins=15)
# axes[1, 0].set_title('Petal Length Distribution', fontsize=10)
# axes[1, 0].set_xlabel('cm', fontsize=10)

# axes[1, 1].hist(petal_w, edgecolor='white', bins=15)
# axes[1, 1].set_title('Petal Width Distribution', fontsize=10)
# axes[1, 1].set_xlabel('cm', fontsize=10)

# Generate a title for the overall figure
# fig.suptitle('Distributions of Measurement Variables', fontsize=13)

# Save a copy of the histograms as a png file
# plt.savefig('histogram.png')

# SUMMARY DATA BY SPECIES

# setosa summary data
# setosa = iris[iris['class'] == 'Iris-setosa'] 
# print(setosa.describe())

# versicolor summary data
# setosa = iris[iris['class'] == 'Iris-versicolor'] 
# print(setosa.describe())

# virginica summary data
# setosa = iris[iris['class'] == 'Iris-virginica'] 
# print(setosa.describe())

# HISTOGRAMS BY SPECIES

# 1. SETOSA
# Create dataframe with Iris-setosa values only
# setosa = iris[iris['class'] == 'Iris-setosa']

# Use matplotlib to plot and style the figure that will house the histogram axes
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(13, 10))
# plt.style.use('ggplot')


# sns.histplot(data=setosa, x="sepal_length_cm", kde=True, ax=axes[0, 0])
# sns.histplot(data=setosa, x="sepal_width_cm", kde=True, ax=axes[0, 1])
# sns.histplot(data=setosa, x="petal_length_cm", kde=True, ax=axes[1, 0])
# sns.histplot(data=setosa, x="petal_width_cm", kde=True, ax=axes[1, 1])

# fig.suptitle('Iris Setosa Distributions', fontsize=20)
# plt.show()

# 2. VERSICOLOR
# Create dataframe with Iris-versicolor values only
# versicolor = iris[iris['class'] == 'Iris-versicolor']

# Use matplotlib to plot and style the figure that will house the histogram axes
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(13, 10))
# plt.style.use('ggplot')


# sns.histplot(data=versicolor, x="sepal_length_cm", kde=True, ax=axes[0, 0])
# sns.histplot(data=versicolor, x="sepal_width_cm", kde=True, ax=axes[0, 1])
# sns.histplot(data=versicolor, x="petal_length_cm", kde=True, ax=axes[1, 0])
# sns.histplot(data=versicolor, x="petal_width_cm", kde=True, ax=axes[1, 1])

# fig.suptitle('Iris Versicolor Distributions', fontsize=20)
# plt.show()

# 3. Virginica
# Create dataframe with Iris-virginica values only
# virginica = iris[iris['class'] == 'Iris-virginica']

# Use matplotlib to plot and style the figure that will house the histogram axes
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(13, 10))
# plt.style.use('ggplot')


# sns.histplot(data=virginica, x="sepal_length_cm", kde=True, ax=axes[0, 0])
# sns.histplot(data=virginica, x="sepal_width_cm", kde=True, ax=axes[0, 1])
# sns.histplot(data=virginica, x="petal_length_cm", kde=True, ax=axes[1, 0])
# sns.histplot(data=virginica, x="petal_width_cm", kde=True, ax=axes[1, 1])

# fig.suptitle('Iris Virginica Distributions', fontsize=20)
# plt.show()





