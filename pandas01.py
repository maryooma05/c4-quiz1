# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:38:28 2024

@author: USER
"""

import pandas as pd
file = pd.read_csv("data_02/iris.csv")

"""
#absolute path:
C:/Users/USER/CSS2024/css2024_day2/data_02/iris.csv

#relative path: 
data_02/iris.csv
"""

#File from a URL
import pandas as pd
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

#url=" https://raw.git......com/xxxxxx/yyy.csv  " this is just any url you may have
#file=pd.read_csv(csv)

#column names
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)


#opening Text file with semi-colon
df = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

#excel sheet
df = pd.read_excel("data_02/residentdoctors.xlsx")

"""
#you can specify which sheet to view
df = pd.read_excel("data_02/residentdoctors.xlsx", sheet="sheet1")
"""

df = pd.read_json("data_02/student_data.json")
print(df)


url="https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"
df= pd.read_csv(url)

#print(df.info())
#print(df.describe())

#df=pd.read_csv("chatfiles/Accelerometer_data.csv", names=["date_time","x","y","z"])


df = pd.read_csv("data_02/country_data_index.csv")

#skipping rows
#df = pd.read_csv("data_02/country_data_index.csv", index_col=0)

df = pd.read_excel("data_02/residentdoctors.xlsx")

print(df.info())

#creating a new column
df["LOWER_AGE"]=df["AGEDIST"].str

#EXTRACTING THE lower rANGE AND PUTTING IT IN A DIFFERENT COLUMN
df["LOWER_AGE"]=df["AGEDIST"].str.extract('(\d+)')


print(df.info())

#added line is still looking like an object so we have to convert to integer so we use the following command
df["LOWER_AGE"]=df["LOWER_AGE"].astype(int)
print(df.info())

#df["LOWER_AGE"]=df["AGEDIST"].str.extract('(\d+)')----EXTRACTING LOWER AGE



#EXTRACTING UPPER AGE
df["UPPER_AGE"]=df["AGEDIST"].str.extract('-(\d+)')

"""

WORKING WITH DATES

10-01-2024 -UK
01-10-2024 -US

"""
#df = pd.read_csv("data_02/time_series_data.csv")


df = pd.read_csv("data_02/time_series_data.csv", index_col=0)
print(df.info())


# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
print(df.info())


#df['Date'] = pd.to_datetime(df['Date'],format="%d-%m-%y")
print(df.info())







