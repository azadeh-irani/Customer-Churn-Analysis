import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
#step1: load dataset
file_path="C:/Users/azade/OneDrive/Desktop/churn_analysis/churn_sheet.xlsx"
df=pd.read_excel(file_path)
#step2:make sure
print(df.head())
# Filter high-risk customers
high_risk_df = df[df['HighRiskFlag'] == 'HighRiskChurn']

# Count high-risk customers by geography
geography_risk_count = high_risk_df['Geography'].value_counts()
print(geography_risk_count)
# Plot High-Risk Customers by Geography
plt.figure(figsize=(10, 6))
sns.barplot(
    x=geography_risk_count.index,  # Geography categories
    y=geography_risk_count.values,  # High-risk customer counts
    palette="viridis"  # Choose a color palette
)
plt.title('High-Risk Customers by Geography', fontsize=16)
plt.xlabel('Geography', fontsize=14)
plt.ylabel('Number of High-Risk Customers', fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y')  # Add gridlines for better interpretation
plt.show()

