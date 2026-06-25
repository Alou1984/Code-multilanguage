import numpy as np
import matplotlib.pyplot as plt
from pyexpat import features

from sklearn.impute import SimpleImputer
from  sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import SGDClassifier
import  seaborn as sns
titanic = sns.load_dataset('titanic')
titanic.head()

y = titanic['survived']
X = titanic.drop('survived', axis = 1)

from sklearn.compose import make_column_transformer, make_column_selector

'''
transformer = make_column_transformer((StandardScaler(), ['age', 'fare']))
transformer.fit_transform(X)
#print(transformer.fit_transform(X))
'''
#parseing numerical and categorial parameter
#numerical_features = ['pclass', 'age','fare']
numerical_features = make_column_selector(dtype_include= np.number)   # select column using include number
#categorical_features = [ 'sex', 'deck', 'alone']
categorical_features = make_column_selector(dtype_exclude=np.number)  # select column using exclude number
    #pipline creation
numerical_pipline = make_pipeline(SimpleImputer(), StandardScaler())    # enlever les valeur null
categorical_pipline = make_pipeline(SimpleImputer(strategy='most_frequent'),OneHotEncoder())   # enlever les valeurs null  et remplacer par les plus frequentes

from sklearn.compose  import make_column_transformer
# make column transform
preprocessor = make_column_transformer((numerical_pipline, numerical_features ),
                                     (categorical_pipline , categorical_features ))
# make the pipline
model = make_pipeline(preprocessor, SGDClassifier())
model.fit(X, y)
print (model.fit (X, y))