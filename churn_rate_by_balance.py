import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
#step1: load dataset
file_path="C:/Users/azade/OneDrive/Desktop/churn_analysis/churn_sheet.xlsx"
df=pd.read_excel(file_path)
#check first rows to make sure correctly loading data
print(df.head())
#create balance range

def categorize_balance(balance):
    if balance <= 10000:
        return '0-10K'
    elif balance <= 50000:
        return '10K-50K'
    elif balance <= 100000:
        return '50K-100K'
    else:
        return '100K+'

# Apply the categorization function
df['BalanceRange'] = df['Balance'].apply(categorize_balance)

churn_by_balance = df.groupby('BalanceRange')['Exited'].mean() * 100
print(churn_by_balance)
plt.figure(figsize=(10, 6))
sns.barplot(
    x=churn_by_balance.index,  # Balance ranges
    y=churn_by_balance.values,  # Churn rates
    palette="coolwarm"
)
plt.title('Churn Rate by Balance Range', fontsize=16)
plt.xlabel('Balance Range', fontsize=14)
plt.ylabel('Churn Rate (%)', fontsize=14)
plt.grid(axis='y')
plt.show()
