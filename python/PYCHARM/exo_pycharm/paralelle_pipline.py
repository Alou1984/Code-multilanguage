import numpy as np
import matplotlib.pyplot as plt
from pyexpat import features
from sklearn.impute import SimpleImputer
from  sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, Binarizer
from sklearn.linear_model import SGDClassifier
import  seaborn as sns
from advanced_pipline import categorical_features

titanic = sns.load_dataset('titanic')
titanic.head()

y = titanic['survived']
X = titanic.drop('survived', axis = 1)

#parseing numerical and categorial parameter
#numerical_features = X[['age','fare']]
from sklearn.compose import make_column_transformer, make_column_selector

numerical_features = make_column_selector(dtype_include = np.number)   # select column  including number
from sklearn.pipeline import make_union

#paralelize transformer
pipeline = make_union(StandardScaler(), Binarizer())
pipeline.fit_transform(numerical_features)
#print(pipeline.fit_transform(numerical_features))

