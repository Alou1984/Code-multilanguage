
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from sklearn.datasets import load_iris

#Loading the iris dataset
iris = load_iris()

x = iris.data
y= iris.target
'''
names = list ( iris.target_names )
plt.figure()

print (f'x contient {x.shape[0]} exemples et {x.shape[1]} variable ')
print(f'il  y a {np.unique (y).size} classes')
#print (x)
#print (y)
#alpha = transpparance
#s= size
#plt.scatter(x[:, 0], x[:, 1], c=y, alpha =0.5, s=100)
plt.scatter(x[:, 0], x[:, 1], c=y, alpha =0.5, s=x[:,2]*100)
plt.xlabel('longueur du sepal')
plt.ylabel('largueur du sepal')
plt.show()
'''

#3D graph 1

from mpl_toolkits.mplot3d import Axes3D
'''
ax= plt.axes(projection= '3d')
plt.scatter(x[:, 0], x[:, 1], x[:, 2], c=y)
plt.show()
'''

#3D graph 2
f=lambda x, y:np.sin(x)+np.cos (x+y)
X = np.linspace(0, 5,100)
Y = np.linspace(0, 5,100)
X,Y =np.meshgrid (X,Y)
Z = f(X,Y)
print (f'Dimension of Z est: {Z.shape}')

ax = plt.axes(projection='3d')
ax.plot_surface (X,Y,Z, cmap= 'plasma' )
plt.show()