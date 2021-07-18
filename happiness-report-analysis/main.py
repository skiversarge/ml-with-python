import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

import os
# for dirname, _, filenames in os.walk('report'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

data = pd.read_csv('report/2019.csv')

# print(data.info())
# print(data.describe())
# print(data.head())
# print(data[data['Country'] == 'Singapore'])

rows_list=[]
for region in data['Region'].unique():
    happinessRankSum = data.loc[data['Region'] == region]['Overall rank'].sum()
    numCountriesInRegion = len(data.loc[data['Region'] == region])
    avgHappinessScorePerRegion = happinessRankSum/numCountriesInRegion;
    dict1 = {'Region': region, 'Happiness Rank Per Region': avgHappinessScorePerRegion, 'numCountriesInRegion': numCountriesInRegion};
    rows_list.append(dict1)

df = pd.DataFrame(rows_list)
df.sort_values(['Happiness Rank Per Region'], ascending=True, inplace=True)
# print(df)

plt.figure(figsize=(10,10))
ax = sns.barplot(df['Region'], df['Happiness Rank Per Region'])
ax.set_xticklabels(ax.get_xticklabels(), rotation=15, ha="right")
plt.show()

