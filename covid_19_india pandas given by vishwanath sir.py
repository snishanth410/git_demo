import pandas as pd
from datetime import datetime,timedelta

covid_data = pd.read_csv(r'C:\Users\Nishanth Selvam\Downloads\Pandas\covid_vaccine_statewise.csv',index_col='Updated On')


import pandas as pd
df=pd.read_csv('D:/Downloads-1/Pandas/employee.csv')
df
name='emp_d'
for i in df['dept_id'].unique():
    




covid_data.head()
covid_data.tail()
covid_data.index

covid_data.index = pd.to_datetime(covid_data.index,format='%d-%m-%Y')

covid_data.fillna(0,inplace=True)

covid_data.replace({'-':'0'},inplace=True)  # replace unknown data as 0

covid_data['ConfirmedIndianNational']=covid_data['ConfirmedIndianNational'].astype(int)   # change type as int instead of object
covid_data['ConfirmedForeignNational']=covid_data['ConfirmedForeignNational'].astype(int)

covid_data.info()

#1) How many confirmed cases in month of march and april?

series = covid_data.loc['2021-03-01':'2021-03-31'].groupby('State/UnionTerritory')

series['Confirmed'].max() - series['Confirmed'].min()

series = covid_data.loc['2021-04-01':'2021-04-30'].groupby('State/UnionTerritory')

series['Confirmed'].max() - series['Confirmed'].min()

#2) in last 2 weeks from the latest record data available - how many deaths happened?

last_2_weeks=covid_data.index.max()-timedelta(days=14)

series = covid_data.loc[last_2_weeks:].groupby('State/UnionTerritory')

series['Deaths'].max() - series['Deaths'].min()

#3) in the states - AP, Kerala, Karnataka - how many cured in March and April

df = covid_data[(covid_data['State/UnionTerritory']=='Andhra Pradesh') | (covid_data['State/UnionTerritory']=='Kerala') | (covid_data['State/UnionTerritory']=='Karnataka')].loc['2021-03-1':'2021-03-31']
df.groupby('State/UnionTerritory')['Cured'].max()

df = covid_data[(covid_data['State/UnionTerritory']=='Andhra Pradesh') | (covid_data['State/UnionTerritory']=='Kerala') | (covid_data['State/UnionTerritory']=='Karnataka')].loc['2021-04-1':'2021-04-30']
df.groupby('State/UnionTerritory')['Cured'].max()

#4) in the last 90 days how many foreign nationals had confirmed cases?

last_90_days=covid_data.index.max()-timedelta(days=90)

series = covid_data.loc[last_90_days:].groupby('State/UnionTerritory')

series['ConfirmedForeignNational'].max() - series['ConfirmedForeignNational'].min()

#5) in the last two months - March and April - which are the two states with highest  confirmed cases?

last_60_days=covid_data.index.max()-timedelta(days=60)

series = covid_data.loc[last_60_days:].groupby('State/UnionTerritory').max()

#Similarly, the two states - having the least cases.

series['Confirmed'].sort_values()[:2]

#6) On which two dates there were highest cases , which states are they?



#take the data from last 50 days from the last record hence, if the last record has May 7th then from that last 50 days should be taken

last_50_days=covid_data.index.max()-timedelta(days=50)

covid_data.loc[last_50_days:]
