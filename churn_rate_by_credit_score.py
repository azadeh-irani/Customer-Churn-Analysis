import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
#step1: load dataset
file_path="C:/Users/azade/OneDrive/Desktop/churn_analysis/churn_sheet.xlsx"
df=pd.read_excel(file_path)
#check first rows to make sure correctly loading data
print(df.head())
#categories by credit score

def categorize_credit_score(score):
    if score <= 400:
        return '300-400'
    elif score <= 500:
        return '401-500'
    elif score <= 600:
        return '501-600'
    elif score <= 700:
        return '601-700'
    else:
        return '701-850'

# Apply the categorization function
df['CreditScoreRange'] = df['CreditScore'].apply(categorize_credit_score)

churn_by_credit = df.groupby('CreditScoreRange')['Exited'].mean() * 100
print(churn_by_credit)
plt.figure(figsize=(10, 6))
sns.barplot(
    x=churn_by_credit.index,  # Credit score ranges
    y=churn_by_credit.values,  # Churn rates
    palette='coolwarm'
)
plt.title('Churn Rate by Credit Score Range', fontsize=16)
plt.xlabel('Credit Score Range', fontsize=14)
plt.ylabel('Churn Rate (%)', fontsize=14)
plt.grid(axis='y')
plt.show()

