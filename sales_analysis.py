import pandas as pd




df = pd.read_csv('sales_data.csv')



print(df.head(2))
print("\n -------------------")
print(df.tail(2))
print("\n -------------------")


print(df.describe())
print("\n -------------------")


df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'])
print("\n -------------------")

df['total sales'] = df['Quantity'] * df['Price']
print(df['total sales'].head())
print("\n -------------------")

uniqueOnes = df['Product'].nunique()
print(uniqueOnes)
print("\n -------------------")

mostSaleSorted = df.groupby('Product')['total sales'].sum().sort_values(ascending=False)
print(mostSaleSorted.head(1))
print("\n -------------------")

avgPriceElec = df[df['Category'] == 'Electronics']['Price'].mean()
print(avgPriceElec)
print("\n -------------------")

print(df['total sales'].sum())
print("\n -------------------")

mostSaleSortedCat = df.groupby('Category')['total sales'].sum().sort_values(ascending=False)
print(mostSaleSortedCat)
print("\n -------------------")

newCostumer = df[df['CustomerSegment'] == 'New']
newCostumerTotal = newCostumer['total sales'].sum()


exCostumer = df[df['CustomerSegment'] == 'Existing']
exCostumerTotal = exCostumer['total sales'].sum()


print(newCostumerTotal)
print(exCostumerTotal)
print("\n -------------------")


