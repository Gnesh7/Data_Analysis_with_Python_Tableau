# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:38:47 2022

@author: User
"""

import pandas as pd 

# file_name = pd.read_csv('file.csv') <---- formate of read csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';' )

#summary of the data 
data.info()

#working with calculations

#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemPurchases = 6

#mathmatical operation on tableau

ProfitPerItem = 21.11-11.73
ProfitPerItem = SellingPricePerItem-CostPerItem

ProfitPerTransaction = NumberofItemPurchases*ProfitPerItem
CostPerTransaction = NumberofItemPurchases*CostPerItem
SellingPricePerTransaction = NumberofItemPurchases*SellingPricePerItem

#CostPerTransaction column Calculation

#CostPerTransaction = CostPerItem*NumberofItemPurchased
#Variable =dataframe['Column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem*NumberofItemsPurchased

#adding a new column ta a data frame
 
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales-Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales-Cost)/Cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

#Rounding Markup

roundmarkup = round(data['Markup'] ,2)

data['Markup'] = round(data['Markup'] ,2)

#Combining date field

my_date = 'Day'+'-'+'Month'+'-'+'Month'

data.info()

#checking column data type
print(data['Day'].dtype)

#change column type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month'] +'-'+ year 

data['date'] = my_date

#unsing iloc to view specific column

data.iloc[0] #views the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #brings in fist 5 rows

data.iloc[:,2] #brings in all rows on the 2nd column

data.iloc[4,2] #brings in 4th rows and 2nd column

#using split to split the client_keyword field
#new_var = Column.str.split('sep', expend=Truw)

split_col = data['ClientKeywords'].str.split(',' , expand=True )

#creating new column for the split column in client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using replace function

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge
#Bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')


#Merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on='Month')

#Dropping Columns
#df = df.drop('columnname', axis=1)

data = data.drop('ClientKeywords', axis=1)

data = data.drop('Day', axis=1)

data = data.drop(['Year', 'Month'], axis=1)

#Export into CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)







































































