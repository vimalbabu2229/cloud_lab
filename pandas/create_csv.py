#TO CREATE CSV FILE 
import pandas as pd
length = []
breadth = []
print("Enter tha values: \n")
for i in range(3):
    length.append(int(input(f"Enter length{i} :")))
    breadth.append(int(input(f"Enter breadth{i} :")))
df = pd.DataFrame({'length': length, 'breadth': breadth})
print(df)
df.to_csv("output/area.csv")
print("Successfully created the file >>> ")