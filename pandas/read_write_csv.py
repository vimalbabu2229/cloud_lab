#TO READ THE CSV FILE WITH LENGTH AND BREADTH AND
#CALCULATE AREA AND APPEND TO THE FILE

import pandas as pd 

df = pd.read_csv('pandas/output/area.csv')
#drop if any unwanted columns exists
df.drop(['Unnamed: 0'], axis=1, inplace=True)
df['area'] = df['length'] * df['breadth']
print(df)
df.to_csv('pandas/output/area.csv', index=False)
print("Successfully modified the csv file with area >>")