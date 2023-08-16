# COMPARISON 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from IPython.display import display

df = pd.read_csv('linear_regression\Melbourne_housing_FULL.csv')
df = df.dropna()
feature_list = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

x = df[feature_list]
y = df['Price']
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state=0)

mae_dict = {}

#Linear regression
from sklearn import linear_model

lin_model = linear_model.LinearRegression()

lin_model.fit(train_x, train_y)

pred_y = lin_model.predict(val_x)

lin_mae = mean_absolute_error(val_y, pred_y)

mae_dict['Linear Regression'] = lin_mae

#Decision Tree
from sklearn.tree import DecisionTreeRegressor

dt_model = DecisionTreeRegressor(random_state=0)

dt_model.fit(train_x, train_y)

pred_y = dt_model.predict(val_x)

dt_mae = mean_absolute_error(val_y, pred_y)

mae_dict['Decision Tree'] = dt_mae

#Random Forest
from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(random_state=0)

rf_model.fit(train_x, train_y)

pred_y = rf_model.predict(val_x)

rf_mae = mean_absolute_error(val_y, pred_y)

mae_dict['Random Forest'] = rf_mae


for model in mae_dict.keys():
	print(f"MAE for {model} = {mae_dict[model]}")

optimal = min(mae_dict, key=lambda x: mae_dict[x])
print(f"\nModel with least error is: {optimal} with error: {mae_dict[optimal]:.2f}")
