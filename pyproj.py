import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Adjust display options
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 5000)
np.set_printoptions(linewidth=5000)

# Read the CSV file
df = pd.read_csv('fls1.csv')

# Group by 'zip_code' and 'item_description' to find the most sold item per zip code
grouped = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum()
sold_max = grouped.groupby('zip_code').idxmax()

# Convert the series into a list
sld=sold_max.tolist()

# Create nested lists instead of tuples
lista=[]
for i in sld:
    lista.append(list(i))

# Select only the second item in the nested list and create a new one - most sold items list
most_sld=[]
for i in lista:
   most_sld.append(i[1])

# Select only the first item in the nested list and create a new one - zip codes list
zip_codes=[]
for i in lista:
   zip_codes.append(str(i[0]))

# Create a scatterplot which shows which item is most sold in each zip code area
plt.figure(figsize=(10,14))
plt.scatter(most_sld, zip_codes, edgecolors= 'r', color= 'black')
plt.xticks(rotation = 90)

plt.show()

grouped1 = df.groupby('store_name')['sale_dollars'].sum()
total = df['sale_dollars'].sum()
sales_perce = grouped1*100/total

# Convert the series into a list
lista1=[]
for i in sales_perce:
    lista1.append(i)

#Create a pie chart to identify easily the percentage of sales per store in the period between 2016-2019
plt.figure(figsize=(20,20))
plt.pie(lista1, labels = sales_perce.index)
plt.legend(title= "percentage of sales per store in the period between 2016-2019", fontsize="5")

plt.show()

"""----------------------------or create a bar plot----------------------------------------------"""

# Create a bar plot chart to identify the percentage of sales per store in the period between 2016-2019
plt.figure(figsize=(10,14))
plt.bar(sales_perce.index, lista1, color='purple')
plt.xlabel("Store Name")
plt.ylabel("Percentage of sales per store in the period between 2016-2019")
plt.xticks(rotation = 90)

plt.show()






