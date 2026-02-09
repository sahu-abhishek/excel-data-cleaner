import pandas as pd

# load data
df = pd.read_csv("sales_data_sample.csv" ,encoding='latin1')

# remove duplicates
df = df.drop_duplicates()

# handle missing values
df = df.fillna(method='ffill')

# convert to proper format (example)
# df['Date'] = pd.to_datetime(df['Date'])

# save cleaned file
df.to_csv("cleaned_sales.csv", index=False)

print("Data cleaned successfully ✅")