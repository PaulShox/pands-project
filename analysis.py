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

# Plot averages of measurement variables for each species
# Set up the structure of the figure and number of axes.
# fig, axes = plt.subplots(2, 2, figsize=(12, 10))
# fig.suptitle('Average Measurements per Species', fontsize=20)
# plt.style.use('ggplot')

# Setup the variable to be plotted and analysed in each axes.
# sns.barplot(data=iris, x='class', y='sepal_length_cm', ax=axes[0, 0], errorbar=None).set(title='Average Sepal Length')
# sns.barplot(data=iris, x='class', y='sepal_width_cm', ax=axes[0, 1], errorbar=None).set(title='Average Sepal Width')
# sns.barplot(data=iris, x='class', y='petal_length_cm', ax=axes[1, 0], errorbar=None).set(title='Average Petal Length')
# sns.barplot(data=iris, x='class', y='petal_width_cm', ax=axes[1, 1], errorbar=None).set(title='Average Petal Width')

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

# 3. VIRGINICA
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





