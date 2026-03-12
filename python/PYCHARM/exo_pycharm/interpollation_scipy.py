import numpy as np
import matplotlib.pyplot as plt
from PIL.GimpGradientFile import linear

x= np.linspace (0,10,10)
y =x**2
'''
plt.scatter(x,y)
plt.show()
'''
from scipy.interpolate import  interp1d
f=interp1d(x,y,kind='linear')
#f=interp1d(x,y,kind='quadratic')
#f=interp1d(x,y,kind='cubic')
#f=interp1d(x,y,kind='nearest')
#f=interp1d(x,y,kind='slinear')
#f=interp1d(x,y,kind='zero')
#f=interp1d(x,y,kind='next')
new_x= np.linspace(0,10,30)
result = f(new_x)

plt.scatter( x, y)
plt.scatter( new_x, result, c='r')
plt.show()
