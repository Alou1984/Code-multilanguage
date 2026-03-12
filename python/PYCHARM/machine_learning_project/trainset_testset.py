import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

from regression_SKlearn import model

iris = load_iris()
X= iris.data
y= iris.target


print(X.shape)
#plt.scatter (X[:,0], X[:,1], c=y, alpha =0.8 )
#plt.show()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split (X, y, test_size= 0.2)
'''
print( 'X_Train set:',X_train.shape)
print( 'X_Test set:',X_test.shape)

plt.figure(figsize=(12,4))
plt.subplots(121)
plt.scatter(X_train[:, 0], X_train[:, 1], c = y_train, alpha = 0.8 )
plt.title('Train set')
plt.subplots(122)
plt.scatter(X_test[:,0], X_test[:, 1], c = y_test, alpha = 0.8 )
plt.title('Test set')
plt.show()
'''
'''
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors= 6)
model.fit(X_train, y_train)
print( 'training score with X_train:' ,model.score(X_train, y_train))
print( 'training score with X_test:' ,model.score(X_test, y_test))
'''
# Validation set ( three set valid , train and test)

# Cross Validation set

from sklearn.model_selection import cross_val_score
#print(cross_val_score (KNeighborsClassifier(), X_train, y_train, cv=5, scoring='accuracy'))

  # mean of score and  and plot it depending the number of neighbors
'''
val_score = []
for k in range (1, 50):
    score = cross_val_score (KNeighborsClassifier(k), X_train, y_train, cv=5, scoring='accuracy').mean()
    val_score.append(score)
plt.plot(val_score)
plt.show()
'''
# Setting hyperparameter

from sklearn.model_selection import GridSearchCV
'''
param_grid = {'n_neighbors':np.arange(1, 20),
                            'metric': ['euclidean','manhattan']}
grid = GridSearchCV(KNeighborsClassifier(),param_grid, cv=5)
print(grid.fit(X_train,y_train))
print(grid.best_score_)
print(grid.best_params_)
model = grid.best_estimator_
model.score(X_test, y_test)
'''

#Learning curve
from sklearn.model_selection import learning_curve

N, train_score, val_score = learning_curve (model, X_train, y_train, train_sizes = np.linspace(0.1,1.0,10), cv=5)

print(N)
plt.plot( N, train_score.mean(axis=1), label ='train')
plt.plot( N, train_score.mean(axis=1), label ='validation')
plt.xlabel('train_sizes')
plt.legend()
plt.show()


