
import numpy as np
import matplotlib.pyplot as plt

#Regression as SKlearn
np.random.seed(0)
m = 100
X = np.linspace(0,10, m).reshape(m, 1)
print("X matrix size")
print(X.shape)
y = X + np.random.randn (m, 1)
print("y matrix size")
print(y.shape)
plt.scatter (X, y)
#plt.show()

from sklearn.linear_model import LinearRegression

# Model creation
model = LinearRegression()
# model learning
model.fit(X,y)
# Preformance estimation  of the model
model.score(X,y)
print(model.score(X,y))
# Prediction  base on teh model
prediction = model.predict(X)
plt.scatter( X, y)
plt.plot(X, prediction, c='r')
plt.show()