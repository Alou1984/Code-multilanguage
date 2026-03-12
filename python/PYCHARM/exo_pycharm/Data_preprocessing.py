import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler, RobustScaler, PolynomialFeatures

from trainset_testset import X_train, y_train

#transformer
'''
y= np.array(['chat', 'chien', 'chat', 'oiseau', 'dinde'])
encoder = LabelEncoder()
encoder.fit_transform(y)
print(encoder.fit_transform(y))
'''
#inverse transform
'''
print(encoder.inverse_transform(np.array([0, 0, 2, 3])))
'''
# One hot  and binarizer encoder

from sklearn.preprocessing import LabelBinarizer
'''
encoder = LabelBinarizer(sparse_output=True)
encoder.fit_transform(y)
print(encoder.fit_transform(y))
'''
#Normalization

from sklearn.datasets import load_iris
'''
iris = load_iris()
X = iris.data
outliers = np.full((10, 4), 100) + np.random.randn (10, 4)
X = np.vstack((X, outliers))

X_minmax = MinMaxScaler().fit_transform(X)
X_stdscl = StandardScaler().fit_transform(X)
X_robust = RobustScaler().fit_transform(X)
plt.scatter(X[:, 2], X[:, 3], alpha = 0.5, label = 'original')
plt.scatter(X_minmax[:, 2], X[:, 3], alpha = 0.5, label = 'min_max')
plt.scatter(X_stdscl[:, 2], X[:, 3], alpha = 0.5, label = 'standard')
plt.scatter(X_robust[:, 2], X[:, 3], alpha = 0.5, label = 'robust')
plt.legend()
plt.show()
'''

#pipline = transformer + Estimator
from sklearn.pipeline import make_pipeline

model = make_pipeline(StandardScaler(), SGDClassifier())
model.fit(X_train, y_train)
model.predict(X_train)


#Grid search cv

from sklearn.model_selection import GridSearchCV
model= make_pipeline(PolynomialFeatures(), StandardScaler(), SGDClassifier(random_state=0))
print(model)