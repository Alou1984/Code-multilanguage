from pickletools import optimize

import numpy as np
import matplotlib.pyplot as plt
from PIL.GimpGradientFile import linear


'''
x= np.linspace (0,2,100)
y =1/3*x**3 -3/5 * x**2 + 2 + np.random.randn(x.shape[0])/20
'''
#plt.scatter (x,y)
#plt.show()
'''

#define a modele

def f(x, a, b, c, d) :
    return a * x**3 + b*x**2 + c*x + d


from scipy import  optimize
#print(optimize.curve_fit (f, x, y))
params, param_cov = optimize.curve_fit (f, x, y)
plt.scatter (x, y)
plt.plot(x, f(x, params[0], params[1], params[2], params[3]), c='g', lw =3)

'''


#Minimisation 2D
'''
from scipy import  optimize
def f(x):
    return  x**2 + 15* np.sin(x)

x = np.linspace(-10,10,100)
#plt.plot (x, f(x))
#plt.show()
x0=-5
#print( optimize.minimize (f, x0 = -5).x)
result = optimize.minimize (f, x0 = x0).x
plt.plot(x, f(x), lw=3, zorder= -1)
plt.scatter(result,f(result), s=100, c= 'r', zorder= 1)
plt.scatter (x0, f(x0), marker='+',s=200, c= 'g', zorder= 1)
plt.show()
'''
#Minimisation 3D
from scipy import  optimize

def f(x):
    return np.sin(x[0]) + np.cos(x[0] +x[1]) * np.cos (x[0])

x = np.linspace (-3, 3,100)
y = np.linspace (-3, 3,100)
x,y = np.meshgrid (x, y)
plt.contour(x, y, f(np.array([x, y])),20)

#Minimize one
x0 = np.zeros((2, 1))
plt.scatter(x0[0], x0[1], marker= '+', c='r', s=100)
result = optimize.minimize(f, x0=x0).x
plt.scatter(result[0], result[1], c='g', s=100)
print(result)

plt.show()

