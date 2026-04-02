import pandas as pd

produtos = {
    'Product': ['Laptop', 'Tablet', 'Smartphone', 'Monitor'],
    'Category': ['Computers', 'Tablets', 'Phones', 'Displays'],
    'Price (€)': [950, 400, 800, 300],
    'Amout Sold': [10, 15, 8, 20]
}

df = pd.DataFrame(produtos)

print("Products and sales:")
print(df)
print()

df['Total Revenew (€)'] = df['Price (€)'] * df['Amount sold']
print("DataFrame with new column (Total Revenew):")
print(df)
print()

df_colunas = df.loc[:, ['Products', 'Total Revenew (€)']]
print("DataFrame with new filterd columns (Products e Total Revenew):")
print(df_colunas)
print()

df = df.drop(columns=['Category'])
print("DataFrame without column 'Category':")
print(df)
print()

df['Category'] = ['Electronics', 'Mobile', 'Devices', 'Acessories']
print("DataFrame with new column 'Category':")
print(df)
print()

df_preco_asc = df.sort_values(by='Price (€)', ascending=True)
print("Products sorted by ascending prices:")
print(df_preco_asc)
print()

df_receita_desc = df.sort_values(by='Total Revenew (€)', ascending=False)
print("Products sorted by descending Total revenew:")
print(df_receita_desc)
print()

filtro_categoria = df[df['Ca'].str.contains('Devices')]
print("Products from the category 'Devices':")
print(filtro_categoria)
print()

filtro_preco = df[df['Price (€)'].between(300, 900)]
print("Products with prices between 300€ - 900€:")
print(filtro_preco)
print()