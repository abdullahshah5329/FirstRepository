
import pandas as pd
#import numpy as np

data = pd.read_csv('Time Americans Spend Sleeping.csv')
data.columns

data1 = data[['Year','Period', 'Avg hrs per day sleeping', 'Type of Days', 'Age Group', 'Activity', 'Sex']]
#data1.head(700)
#print(data1.tail(630))
#data1.drop()
data2 = data1.loc[315:]

print(data2)


data2.to_csv('NewTimeAmericansSpendSleeping.csv')
