
import numpy as np
import matplotlib.pyplot as plt
import  pandas as pd
import  seaborn as sns


#Titanic survivor

titanic = sns.load_dataset('titanic')
#print(titanic.shape)
#print(titanic.head())

titanic = titanic[['survived','pclass', 'sex', 'age']]
titanic.dropna(axis = 0, inplace = True)  # delete  lin with 'na'

#Replace  male - 0 ans  female - 1

#titanic['sex'].replace(['male','female'],[0, 1],inplace =True)
pd.set_option('future.no_silent_downcasting', True)
titanic['sex']=titanic['sex'].replace('male', 0)
titanic['sex']=titanic['sex'].replace('female', 1)

#print(titanic.head())

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
y = titanic['survived']
X = titanic.drop('survived', axis = 1)
# Trainning of the model
model.fit(X,y)
# scoring of te model
model.score(X, y)
print(model.score(X, y))
#prediction of the model
Z= model.predict(X)
#print (Z)

def surviver ( model, pclass=1, sex=0, age=40):
    x= np.array([pclass, sex, age]).reshape(1, 3)
    print(model.predict(x))
    print(model.predict_proba(x))
surviver(model)

