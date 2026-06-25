import matplotlib.pyplot as plt
from sklearn.feature_selection import VarianceThreshold
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
plt.plot(X)
plt.legend(iris.feature_names)
#plt.show()
X.var(axis=0)
print(X.var(axis=0))

selector = VarianceThreshold(threshold= 0.2)
selector.fit_transform(X)
print(selector.fit_transform(X))
selector.get_support()
print(selector.get_support())