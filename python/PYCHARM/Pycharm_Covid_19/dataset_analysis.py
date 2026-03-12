import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import imshow, figure

pd.set_option('display.max_row', 111)
pd.set_option('display.max_column', 111)
data = pd.read_excel('dataset_covid.xlsx')
#print(data.head())

# Form Analysis
    # identification
df = data.copy()
    # Matrix
print(df.shape)
    # Var type
df.dtypes.value_counts()
#print(df.dtypes.value_counts())
    # Nan val
df.isna()
#plt.figure(figsize =(18,9) )
#sns.heatmap(df.isna(), cbar=False) # valeur maquantes
#plt.show()
(df.isna().sum()/df.shape[0]).sort_values(ascending = True) # Tri de la somme of nan value
#print((df.isna().sum()/df.shape[0]).sort_values(ascending=True))
# delete data with 90% de données manquant
#df.columns[df.isna().sum()/df.shape[0]<0.9] # Tri de la somme of nan value
#print(df.columns[df.isna().sum()/df.shape[0]<0.9])
df =df[df.columns[df.isna().sum()/df.shape[0]<0.9]  ]   #injection dans data frame
#print(df.head())
print(df.shape)
#sns.heatmap(df.isna(), cbar=False) # valeur maquante
#plt.figure(figsize =(18,9) )
#sns.heatmap(df.isna(), cbar=False) # valeur maquante
#plt.show()
# Drop column
df = df.drop( 'Patient ID', axis=1)
#Number of test realised
df['SARS-Cov-2 exam result'].value_counts()
print(df['SARS-Cov-2 exam result'].value_counts(normalize=True))
# Deep Analysis
    # Target visualization ( histo/Boxplot)
        #Float var
'''
for col in df.select_dtypes('float'):
    #print (col)
    plt.figure()
    sns.displot(df[col])
plt.show()
'''
        #Age
'''      
print(df['Patient age quantile'].value_counts())
sns.displot(df['Patient age quantile'])
plt.show()
'''
        #Qualitative variable
'''
for col in df.select_dtypes('object'):
    print (f'{col:-<50} {df[col].unique()}')  # formated string
'''
'''
for col in df.select_dtypes('object'):
    plt.figure()
    df[col].value_counts().plot.pie()
    plt.show()
'''
# Relation between variable
positive_df =df[df['SARS-Cov-2 exam result'] =='positive']            #boolean indexing  all positif
negative_df =df[df['SARS-Cov-2 exam result'] =='negative']            #boolean indexing  all negative
missing_rate = df.isna().sum()/df.shape[0]                            # rate of missing dat
blood_columns = df.columns [(missing_rate < 0.9 )& (missing_rate > 0.88 )] # value  between 0.88 and 0.8
viral_columns = df.columns [(missing_rate < 0.88 )& (missing_rate > 0.75 )] # value  between 0.88 and 0.8
#relation  target and variable
'''
for col in blood_columns:
    plt.figure()
    sns.displot(positive_df[col], label ='positive')
    sns.displot(negative_df[col], label='negative')
    plt.legend()
    plt.show()
'''
    #Relation target/age
'''  
sns.countplot(x='Patient age quantile', hue='SARS-Cov-2 exam result', data = df)
plt.show()
'''
    #relation  Target/viral
'''
pd.crosstab(df['SARS-Cov-2 exam result'], df['Influenza A'])    # afficher la table
print(pd.crosstab(df['SARS-Cov-2 exam result'], df['Influenza A'])) # cross table  between 'SARS-Cov-2 exam result' and  'Influenza A' verus

for col in viral_columns:
    plt.figure()
    sns.heatmap(pd.crosstab(df['SARS-Cov-2 exam result'], df[col]), annot= True,fmt ='d')
    plt.show()  
'''
# Detailled relation variables /variables
#   relation taux sanguin
'''
#sns.pairplot(df[blood_columns])  # display all tables
#sns.heatmap(df[blood_columns].corr())  # display correlation of column of  all tables
sns.clustermap(df[blood_columns].corr())  # display correlation of column of  all tables
plt.show()
'''
#   relation Age / sang
'''
for col in blood_columns:
    plt.figure()
    sns.lmplot(x='Patient age quantile',y=col, hue='SARS-Cov-2 exam result', data = df)
    #plt.show()
'''

df.corr()
#print(df.corr())
    # Understand of diff var (interNET
    # Feature-Target visualization ( histo/Boxplot)
    # Outliers visualization