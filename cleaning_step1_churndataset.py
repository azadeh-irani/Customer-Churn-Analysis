import pandas as pd

# Use one of the corrected methods for the file path
df = pd.read_csv(r"C:\Users\azade\OneDrive\Desktop\churn_analysis\Churn_Modelling.csv")

# Check data types
print(df.dtypes)
#finding missing values
print(df.isnull().sum())
#validate data range and unique values
print(df.describe())
missing_customer_ids = df[df['CustomerId'].isnull()]
print(missing_customer_ids)
empty_customer_ids = df[df['CustomerId'].astype(str).str.strip() == '']
print(empty_customer_ids)


# Check the total number of rows in the dataset
print("Total Rows in Dataset:", len(df))

# Count non-null values in CustomerId
print("Non-Null CustomerId Count:", df['CustomerId'].notnull().sum())

# Count unique CustomerId values
print("Unique CustomerId Count:", df['CustomerId'].nunique())
# Identify duplicate CustomerId values
duplicates = df[df['CustomerId'].duplicated()]
print(duplicates)


print(df['Geography'].unique())
print(df['Gender'].unique())


print(df['HasCrCard'].unique())
print(df['IsActiveMember'].unique())
print(df['Exited'].unique())


df.to_csv("cleaned_Churn_Modelling.csv", index=False)


