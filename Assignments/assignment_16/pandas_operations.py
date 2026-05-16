import pandas as pd

raw_data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Laptop', 'Mouse', None],
    'Revenue': [1200, 25, 300, 75, 1150, None, 150],
    'Cost': [800, 10, 200, 40, 850, 15, 100],
    'Date': ['2025-01-10', '2025-02-15', '2025-03-20', '2025-10-05', '2025-11-12', '2025-12-25', '2025-06-01']
}
df = pd.DataFrame(raw_data)

# 1. Handle Missing Values
df['Revenue'] = df['Revenue'].fillna(df['Revenue'].median())
df['Product'] = df['Product'].fillna("Unknown")

# 2. Feature Engineering
df['Profit'] = df['Revenue'] - df['Cost']
df['Margin_Percentage'] = (df['Profit'] / df['Revenue']) * 100

# 3. Filtering for Q4 (Months 10, 11, 12) and Profit > 50
df['Date'] = pd.to_datetime(df['Date'])
q4_filtered_df = df[(df['Date'].dt.month.isin([10, 11, 12])) & (df['Profit'] > 50)]

print("Cleaned DataFrame:\n", df)
print("\nFiltered Q4 DataFrame:\n", q4_filtered_df)
