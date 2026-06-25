# anomaly detection
import matplotlib.pyplot as plt
import numpy as np
from numpy.ma.core import argmax
from sklearn.ensemble import IsolationForest
from sklearn.feature_selection import VarianceThreshold
from sklearn.datasets import  make_blobs
'''
X, y = make_blobs(n_samples = 50, centers = 1, cluster_std= 0.1, n_features= 2, random_state=0)
X[-1,:]= np.array([2.25,5])
plt.scatter(X[:,0], X[:,1])
#plt.show()
from sklearn.ensemble import IsolationForest
model = IsolationForest (contamination=0.01)  # percentage of contamination =1%
model.fit(X)
plt.scatter(X[:,0], X[:,1], c=model.predict(X)) # isolation of the outlayer
plt.show()
'''
# Decontamination digit
from sklearn.datasets import load_digits
digits= load_digits()
images = digits.images
X = digits.data
y = digits.target
print(X.shape)

# display on image
'''
plt.imshow(images[42])
plt.show()
'''
# detection of anomaly
'''
model = IsolationForest(random_state=0, contamination=0.02)
model.fit(X)
model.predict(X)
print(model.predict(X)) # predict(X) -> if 1 = normal , if -1 = anomaly
'''
# See some outliers with boolean indexing
'''
outliers = model.predict(X) == -1
print("outliers are true: ", outliers ) # Outliers
print (images [outliers])
 #print first image
print ('first image')
plt.imshow(images[outliers][0])
plt.title(y[outliers][0])
plt.show()
'''
# Dimension reduction PCA (Composent Analyse principal) with standard data for process continu data
from sklearn.decomposition import PCA
'''
X.shape
model =PCA(n_components=2)   # 2D
X_reduced = model.fit_transform(X)
plt.scatter(X_reduced[:,0], X_reduced[:,1], c=y)
plt.colorbar()
#plt.show()
print ('component content: ', model.components_)  # le contenu de chaque composant
print ('component shape: ', model.components_.shape)  # le contenu de chaque composant
'''

#Data compression
model = PCA(n_components=64)
X_reduced = model.fit_transform (X)
np.cumsum (model.explained_variance_ratio_)   # pourcentage de variance
print(np.argmax (np.cumsum (model.explained_variance_ratio_)>99)) # argmax
print(np.cumsum (model.explained_variance_ratio_) )
plt.plot(np.cumsum (model.explained_variance_ratio_))
plt.show()