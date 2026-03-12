
import numpy as np
import matplotlib.pyplot as ptl
import pandas as pd

# Install pip install pandas openpyxl
data = pd.read_excel('titanic_xlsx.xlsx')
#print(data.shape)
print (data.head())
#print (data.columns)

# Eliminate column
data = data.drop (['name', 'sibsp', 'ticket','fare', 'cabin','embarked','boat','body','home.dest'], axis=1)
#print(data.shape)
#print (data.head())
#print (data.columns)

#description of data (mean, poucentatge, std, min, max )
#print(data.describe())

#Eliminate data wit line with NA in age
data = data.dropna(axis= 0)
#print(data.shape)
#print(data.describe())

# Data counted in a table
#print(data['pclass'].value_counts().plot.bar())
#ptl.show()

#Grouped by column carac
#print(data.groupby(['pclass','sex']).mean())

#indexing localisation (sur ligne )
print(data.iloc[0:2,0:2])

#indexing localisation (sur ligne )
print(data.loc[0:2,['age', 'sex']])

