# LINEAR REGRESSION - DECISION TREE
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error


housing_data=pd.read_csv('linear_regression\Melbourne_housing_FULL.csv')
housing_data=housing_data.dropna(axis=0)
housing_features=['Rooms','Bathroom','Landsize','Lattitude','Longtitude']
x=housing_data[housing_features]
y=housing_data.Price

train_x,val_x,train_y,val_y=train_test_split(x,y,random_state=0)

model=DecisionTreeRegressor(random_state=1,max_depth=10)
model.fit(train_x,train_y)
y_pred=model.predict(val_x)
y_pred1=pd.DataFrame(y_pred)
print(val_x.head())
print('\n     price')
print(y_pred1.head())
mae=mean_absolute_error(val_y,y_pred)
mse=mean_squared_error(val_y,y_pred)
print("MAE:",mae)
print("MSE:",mse)