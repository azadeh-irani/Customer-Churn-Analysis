import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
#step1: load dataset
file_path="C:/Users/azade/OneDrive/Desktop/churn_analysis/churn_sheet.xlsx"
df=pd.read_excel(file_path)
#step2:make sure
print(df.head())
churn_by_activity = df.groupby('IsActiveMember')['Exited'].mean() * 100
print(churn_by_activity)
plt.figure(figsize=(8, 5))
sns.barplot(
    x=churn_by_activity.index.map({0: 'Inactive', 1: 'Active'}),  # Map activity status to labels
    y=churn_by_activity.values,
    palette='coolwarm'
)
plt.title('Churn Rate by Activity Status', fontsize=16)
plt.xlabel('Activity Status', fontsize=14)
plt.ylabel('Churn Rate (%)', fontsize=14)
plt.grid(axis='y')
plt.show()
