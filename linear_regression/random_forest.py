import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

file_path = 'linear_regression\Melbourne_housing_FULL.csv'

home_data = pd.read_csv(file_path)
home_data = home_data.dropna(axis=0)
y = home_data.Price

features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
x = home_data[features]

train_x, val_x, train_y, val_y = train_test_split(x, y, random_state=0)

model = RandomForestRegressor(random_state=0)
model.fit(train_x, train_y)

val_predictions = model.predict(val_x)
print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(model.predict(x.head()))
print(f"MAE: {mean_absolute_error(val_y,val_predictions)}")
