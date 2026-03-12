

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset ('titanic')
#print(titanic.head())

print('Raw data of titanic')
print(titanic.head())
print('Data of titanic filtered ')
titanic.drop(['alone', 'alive', 'who','adult_male', 'embark_town', 'class'], axis = 1, inplace = True)
print(titanic.head())
sns.pairplot(titanic)
plt.show()


#category of plot
'''
titanic.drop(['alone', 'alive', 'who','adult_male', 'embark_town', 'class'], axis = 1, inplace = True)
print(titanic.head())
sns.catplot(x='pclass', y='age', data=titanic, hue= 'sex')
plt.show()
'''
#box plot

#titanic.drop(['alone', 'alive', 'who','adult_male', 'embark_town', 'class'], axis = 1, inplace = True)
'''
print(titanic.head())
sns.boxplot(x='pclass', y='age', data=titanic, hue= 'sex')
plt.show()
'''
#Distribution
'''
sns.displot(titanic['fare'])
plt.show()
'''
#jointure
'''
sns.jointplot('age','sex' ,data = titanic, kind= 'kde')
plt.show()
'''
# Marginal distribution
'''
sns.set_theme(style="darkgrid")
    # Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")
    # Plot the responses for different events and regions
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)
plt.show()
'''

#Joint and marginal histograms

'''
sns.set_theme(style="ticks")

# Load the planets dataset and initialize the figure
planets = sns.load_dataset("planets")
g = sns.JointGrid(data=planets, x="year", y="distance", marginal_ticks=True)

# Set a log scaling on the y axis
g.ax_joint.set(yscale="log")

# Create an inset legend for the histogram colorbar
cax = g.figure.add_axes([.15, .55, .02, .2])

# Add the joint and marginal histogram plots
g.plot_joint(
    sns.histplot, discrete=(True, False),
    cmap="light:#03012d", pmax=.8, cbar=True, cbar_ax=cax
)
g.plot_marginals(sns.histplot, element="step", color="#03012d")
plt.show()

'''

#Annotated heatmaps
'''
sns.set_theme()
# Load the example flights dataset and convert to long-form
flights_long = sns.load_dataset("flights")
flights = (
    flights_long
    .pivot(index="month", columns="year", values="passengers")
)
# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)
plt.show()
'''