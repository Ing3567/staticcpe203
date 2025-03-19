import pandas as pd
from cleandata import cleandata
import seaborn as sns
from chart import chart
import matplotlib.pyplot as plt
from p_value import p_value

dp = pd.read_csv('survey.csv')

# ปรับการตั้งค่าให้แสดงข้อมูลทั้งหมด

pd.set_option('display.max_columns', None)  # แสดงทุกคอลัมน์

dp=cleandata(dp)

print(dp.head())
for column in dp.columns:
    if(column != 'comments'):
        print(f'{column}: {dp[column].unique()}\n')



sns.set_theme()
while (True):
    type = input('chart or p-value: ')
    if(type == 'chart'):
        chart(dp)
    elif(type == 'p-value'):
        p_value(dp)
