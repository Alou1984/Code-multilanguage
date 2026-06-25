import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from sklearn.datasets import load_iris

#Loading the iris dataset
iris = load_iris()

x = iris.data
y= iris.target
names = list ( iris.target_names )

print (f'x contient {x.shape[0]} exemples et {x.shape[1]} variable ')
print(f'il  y a {np.unique (y).size} classes')
# binary instance  is the number of sequence

#plt.hist(x[:,0],bins=15)

# several histo on same graphe
'''
plt.hist(x[:,0],bins=15)
plt.hist(x[:,1],bins=15)
plt.hist(x[:,2],bins=15)
plt.hist(x[:,3],bins=15)
plt.show()
'''
#Histogram 2D with 2 var
'''
plt.hist2d(x[:,0],x[:,1],bins=15)
plt.xlabel('longueur du sepal')
plt.ylabel('largueur du sepal')
plt.colorbar()
plt.show()
'''

#distribution of grille level for a image
'''
from scipy import misc
face = misc.face (gray = True)
#plt.imshow (face, cmap='gray')
plt.hist(face.ravel(),bins= 255)
plt.show()

'''
# Contor plot
'''
f=lambda x, y:np.sin(x)+np.cos (x+y)
X = np.linspace(0, 5,100)
Y = np.linspace(0, 5,100)
X,Y =np.meshgrid (X,Y)
Z = f(X,Y)
#plt.contour(X,Y,Z, 20, colors= 'red')
plt.contourf(X,Y,Z, 20, cmap= 'RdGy')
plt.colorbar()
plt.show()
'''

#sub plot in a same fifgure

#a creation d'un group de 4 dataset
dataset= {f"experience {i}": np.random.randn(100, 4) for i in range (6)}
def graphique (data):
    n= len(data)
    plt.figure(figsize = (12,30))

    for k, i in zip (data.keys(), range (1, n+1)):
        plt.subplot(n,1, i)
        plt.plot(data[k])
        plt.title(k)
    plt.show()


graphique(dataset)