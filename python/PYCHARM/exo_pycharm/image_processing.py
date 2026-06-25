
import numpy as np
import matplotlib.pyplot as plt


from scipy import ndimage
'''
np.random.seed(0)
X = np.zeros((32, 32))
X[10:-10, 10:-10] = 1
X[np.random.randint(0,32,30), np.random.randint(0,32,30)] = 1
plt.imshow(X)

image = plt.imread('bactery.png')
print(image.shape)
'''
#reduce image in 2D
image = plt.imread('bactery.png')
image = image[:,:,0]
plt.imshow (image, cmap='gray')

print(image.shape)
#flatten the image_2
image_2 = np.copy(image)
plt.hist(image_2.ravel(), bins = 255)
plt.show()
