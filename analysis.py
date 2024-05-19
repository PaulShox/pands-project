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
print(iris.head(5))

# Assign Column titles to dataset
iris.columns = [
                'sepal_length_cm', 
                'sepal_width_cm', 
                'petal_length_cm', 
                'petal_width_cm',
                'class'
                ]     

# Check that Column titles have assigned as expected.
print(iris.head(5))   

# Check all 150 rows have imported and that there are no null values
print(iris.info())         

# SUMMARY DATA
# Generate summary data for the numerical variables.
print(iris.describe())

# Assign a variable to the summary dataframe.
summary = iris.describe() 

# Export the summary dataframe as a txt file
summary.to_string('summary.txt')

# SUMMARY DATA BY MEASUREMENT VARIABLE

# # Generate summary data for sepal length for each species
print(iris.groupby(['class']).describe()['sepal_length_cm'])

# Generate summary data for sepal width for each species
print(iris.groupby(['class']).describe()['sepal_width_cm'])

# Generate summary data for petal length for each species
print(iris.groupby(['class']).describe()['petal_length_cm'])

# Generate summary data for petal width for each species
print(iris.groupby(['class']).describe()['petal_width_cm'])

# SUMMARY DATA BY SPECIES

# setosa summary data
setosa = iris[iris['class'] == 'Iris-setosa'] 
print(setosa.describe())

# versicolor summary data
setosa = iris[iris['class'] == 'Iris-versicolor'] 
print(setosa.describe())

# virginica summary data
setosa = iris[iris['class'] == 'Iris-virginica'] 
print(setosa.describe())

# Plot averages of measurement variables for each species
# Set up the structure of the figure and number of axes.
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Average Measurements per Species', fontsize=20)
plt.style.use('ggplot')

# Setup the variable to be plotted and analysed in each axes.
sns.barplot(data=iris, x='class', y='sepal_length_cm', ax=axes[0, 0], errorbar=None).set(title='Average Sepal Length')
sns.barplot(data=iris, x='class', y='sepal_width_cm', ax=axes[0, 1], errorbar=None).set(title='Average Sepal Width')
sns.barplot(data=iris, x='class', y='petal_length_cm', ax=axes[1, 0], errorbar=None).set(title='Average Petal Length')
sns.barplot(data=iris, x='class', y='petal_width_cm', ax=axes[1, 1], errorbar=None).set(title='Average Petal Width')

plt.show()

# SETOSA SEPAL WIDTH INVESTIGATION

# Standard Deviation of Setosa Sepal Widths

# Create a dataframe with Setosa data only.
seto = iris[iris['class'] == 'Iris-setosa']
# Generate the standard deviation for the sepal width column only. 
sd = seto['sepal_width_cm'].std()
# Round the figure to 5 decimal places.
round(sd, 5) 
print(sd)

# Boxplot for Setosa sepal widths.

# Create a dataframe with Setosa data only.
seto = iris[iris['class'] == 'Iris-setosa']
# Generate a boxplot for the sepal width column only
seto.boxplot(['sepal_width_cm'])
plt.show()



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

# Add a Kernel Density Estimate (KDE) Plot to the Combined Histograms

# Setup the structure of the figure and number of axes.
sns.set_style('darkgrid')
fig, axes = plt.subplots(2, 2, figsize=(13, 10))
fig.suptitle('Distributions of Measurement Variables \nAll Species Combined - Including KDE', fontsize=15)

# Setup the variables to be plotted and analysed in each axes. Use kde=True to add the Kernel Density Estimate
sns.histplot(ax=axes[0, 0], data=iris, x='sepal_length_cm', bins=20, kde=True).set(title='Sepal Lengths')
sns.histplot(ax=axes[0, 1], data=iris, x='sepal_width_cm', bins=20, kde=True).set(title='Sepal Widths')
sns.histplot(ax=axes[1, 0], data=iris, x='petal_length_cm', bins=20, kde=True).set(title='Sepal Lengths')
sns.histplot(ax=axes[1, 1], data=iris, x='petal_width_cm', bins=20, kde=True).set(title='Petal Widths')

plt.show()

# HISTOGRAMS BY SPECIES

# 1. SETOSA
# Create dataframe with Iris-setosa values only
setosa = iris[iris['class'] == 'Iris-setosa']

# Use matplotlib to plot and style the figure that will house the histogram axes
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(13, 10))
plt.style.use('ggplot')

# Setup the variables to be plotted and analysed in each axes. Use kde=True to add the Kernel Density Estimate
sns.histplot(data=setosa, x="sepal_length_cm", kde=True, ax=axes[0, 0])
sns.histplot(data=setosa, x="sepal_width_cm", kde=True, ax=axes[0, 1])
sns.histplot(data=setosa, x="petal_length_cm", kde=True, ax=axes[1, 0])
sns.histplot(data=setosa, x="petal_width_cm", kde=True, ax=axes[1, 1])

fig.suptitle('Iris Setosa Distributions', fontsize=20)
plt.show()

# 2. VERSICOLOR
# Create dataframe with Iris-versicolor values only
versicolor = iris[iris['class'] == 'Iris-versicolor']

# Use matplotlib to plot and style the figure that will house the histogram axes
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(13, 10))
plt.style.use('ggplot')

# Setup the variables to be plotted and analysed in each axes. Use kde=True to add the Kernel Density Estimate
sns.histplot(data=versicolor, x="sepal_length_cm", kde=True, ax=axes[0, 0])
sns.histplot(data=versicolor, x="sepal_width_cm", kde=True, ax=axes[0, 1])
sns.histplot(data=versicolor, x="petal_length_cm", kde=True, ax=axes[1, 0])
sns.histplot(data=versicolor, x="petal_width_cm", kde=True, ax=axes[1, 1])

fig.suptitle('Iris Versicolor Distributions', fontsize=20)
plt.show()

# 3. VIRGINICA
# Create dataframe with Iris-virginica values only
virginica = iris[iris['class'] == 'Iris-virginica']

# Use matplotlib to plot and style the figure that will house the histogram axes
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(13, 10))
plt.style.use('ggplot')

# Setup the variables to be plotted and analysed in each axes. Use kde=True to add the Kernel Density Estimate
sns.histplot(data=virginica, x="sepal_length_cm", kde=True, ax=axes[0, 0])
sns.histplot(data=virginica, x="sepal_width_cm", kde=True, ax=axes[0, 1])
sns.histplot(data=virginica, x="petal_length_cm", kde=True, ax=axes[1, 0])
sns.histplot(data=virginica, x="petal_width_cm", kde=True, ax=axes[1, 1])

fig.suptitle('Iris Virginica Distributions', fontsize=20)
plt.show()

# CORRELATION ANALYSIS
# PLOTTING CORRELATIONS

# Create Datframe 
measures = iris[
                ['class',
                'sepal_length_cm',
                'sepal_width_cm',
                'petal_length_cm',
                'petal_width_cm']
]
# Use pairplot to create correlation plot
pairplot(measures, hue='class', diag_kind='hist')
plt.show()


# PLOT A LINE OF BEST FIT BETWEEN TWO VARIABLES
# Use Seaborn to plot lines of best fit between only two variables on the pairplot
sns.pairplot(iris, 
#             # Set the y-axis variable as sepal length
             y_vars=['sepal_length_cm'], 
#              # Set the x-axis variable as petal length
             x_vars=['petal_length_cm'], 
#              # Seaborn regplot
             kind='reg', 
             height=5, 
#              # Sets the ratio of the width to the height
             aspect=1.2,
#              # Formats the colours and size of the line and scatter plot data points
             plot_kws={'ci' : None, 'color' : 'red',
                       'scatter_kws' : {'color' : 'blue'}}
             ).set(title='Line of Best Fit - Sepal Length v Petal Length')
plt.show()

# APPLY LINES OF BEST FIT TO ALL AXES IN THE CORRELATION FIGURE
sns.pairplot(measures, 
            # reg is short for regplot and is used to apply the lines of best fit
            kind='reg', 
            height=2.5,
            # Sets the ratio of the width to the height
            aspect=1,
            # Formats the colours and size of the line and scatter plot data points
            plot_kws={'ci' : None, 'color' : 'red', 
                      'scatter_kws' : {'color' : 'blue', 's' : 4}
                      },
            # Sets the colour of the kernel density estimates in the diagonals
            diag_kws={'color' : 'grey'}
            ).fig.suptitle('Lines of Best Fit', y=1.03)
plt.show()

# CALCULATE CORRELATION COEFFICIENTS
# Assign variables to petal length and petal width
plen = iris['petal_length_cm']
pwth = iris['petal_width_cm']

# Run numpy corrcoef functionality
print(np.corrcoef(plen, pwth))

# CORRELATION MATRIX FOR ALL MEASUREMENT VARIABLES
# Create a dataframe containing only the measurement variables
corr_matrix = iris[
                ['petal_length_cm',
                 'petal_width_cm',
                 'sepal_length_cm',
                 'sepal_width_cm']
]
# Apply the Pandas corr() method to generate corellation matrix dataframe 
corr = corr_matrix.corr()
# Display values
print(corr)

# CORRELATION HEATMAP
# Generate correlation heatmap from correlation matrix in 5.4 above. 
sns.heatmap(corr, 
            # Set minimum value to minus 1
            vmin=-1,
            # Set maximum value to 1 
            vmax=1, 
            # Assign colours to the heatmap
            cmap='PiYG',
            # Assign values to each square in the heatmap 
            annot=True,
            # Format how values appear in each square of the heatmap
            annot_kws={'fontsize' : 12, 
                       'fontweight' : 'bold'
                       },
            # Create a white line between each square in the heatmap
            linewidth=0.5,
            )
plt.show()
