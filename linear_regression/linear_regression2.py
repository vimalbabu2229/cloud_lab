import numpy as np 
from sklearn import linear_model
import matplotlib.pyplot as plt 

x = np.array([1, 2, 3 , 4, 5, 6]).reshape(-1, 1)
y = np.array([2, 22, 16, 34, 6, 10 ]).reshape(-1, 1)

model = linear_model.LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
print(y_pred)

plt.scatter(x, y, color='b')
plt.plot(x, y_pred, color='g')#regression line
plt.xlabel('x_values')
plt.ylabel('y_values')
plt.show()
#scikit-learn