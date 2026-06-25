import matplotlib.pyplot as plt
from sklearn.feature_selection import VarianceThreshold
from sklearn.datasets import  make_blobs
from sklearn.linear_model import SGDClassifier

'''
KMeans (minimisation fo the variance : inerthia  :  Iterative algo which works in 2 steps:
- assigment of centroid in the middle  of the nearst group of points  
- Moove of centroid at the middlle  mean of the cluster
'''

X, y = make_blobs(n_samples = 100, centers = 3, cluster_std= 1.0, n_features= 2, random_state=0)

plt.scatter(X[:,0], X[:,1])

#plt.show()
from sklearn.cluster import KMeans

model = KMeans(n_clusters= 3)
model.fit(X)
model.predict(X)
#print(model.predict(X))

plt.scatter(X[:,0], X[:,1], c=model.predict(X))
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], c='r')

plt.show()
#indice inertia
'''
model.inertia_
print('inertia:',model.inertia_)
model.score(X)
print('Score:',model.score(X))
'''
#Elbow Method; Find the optimal number of cluster for  a dataset
# ( minimisation of teh cost of inertia_ = elbow (coude de la fonction cout )
'''
inertia =[]
K_range =range(1, 20)
for k in K_range:
    model= KMeans( n_clusters=k).fit(X)
    inertia.append(model.inertia_)
plt.plot(K_range, inertia)
plt.xlabel ( "nbr of cluster")
plt.ylabel ( "cost of inertia model")
plt.show()
'''