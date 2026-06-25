from cProfile import label

import numpy as np
import matplotlib.pyplot as plt

# Plot  a function  y= x**2
'''
x= np.linspace(0, 2,10)
y=x**2
print (y)
#plt.plot(x,y)
#plt.scatter(x,y, c="blue", lw=5, ls='--')
#use of figure
plt.figure()
#plt.plot(x,y)
plt.plot(x,x**2)
plt.title("figure1")
plt.xlabel("axe x")
plt.ylabel("axe y")
#plt.legend(['blue'], ['green'], loc=)
#plt.legend()
plt.show()
plt.savefig ('fig_1.png')
'''

# Sub plot function
'''
plt.figure()
x= np.linspace(0, 2,10)
y=x**2
plt.subplot(2,1,1)
plt.plot(x,y, c='red')
plt.title ('grafical 1')
plt.subplot(2,1,2)
plt.plot(x,np.sin(x), label='sinus')
plt.plot(x,np.cos(x) , label='cosinus')
plt.legend()
plt.title ('grafical 2')
plt.show()
'''
#3D graphical

from mpl_toolkits.mplot3d import Axes3D
ax = plt.axes(projection='3d')
ax.scatter(x[:,0],x[:,1],x[:,2], )


