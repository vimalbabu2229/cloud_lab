# LINEAR REGRESSION
import pandas as pd
# import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

data = pd.read_csv('linear_regression\Melbourne_housing_FULL.csv')

feature_list = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
x = data[feature_list]
y = data['Price']
model = LinearRegression()
model.fit(x, y)

#predictions on the training set
y_pred = model.predict(x)

mse = mean_squared_error(y, y_pred)

print(f"Mean squared error: {mse}")
plt.scatter(y, y_pred)
# plt.plot(x, y_pred, color='g')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs. Predicted Prices')
plt.show()