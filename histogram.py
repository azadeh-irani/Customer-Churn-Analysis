import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
#step1: load dataset
file_path="C:/Users/azade/OneDrive/Desktop/churn_analysis/churn_sheet.xlsx"
df=pd.read_excel(file_path)
#check first rows to make sure correctly loading data
print(df.head())
#step2:plot churn distribution 
#create histogram to visualize distribution of churn prediction score
plt.figure(figsize=(10, 6))  # Set the figure size for better readability
sns.histplot(
    df['ChurnPredictionScore'],  # Data column to plot
    bins=20,  # Number of bins for the histogram
    kde=True,  # Include a kernel density estimate curve
    color='blue'  # Set the color of the bars
)
plt.title('Churn Prediction Score Distribution', fontsize=16)  # Add a title
plt.xlabel('Churn Prediction Score', fontsize=14)  # Label the x-axis
plt.ylabel('Customer Count', fontsize=14)  # Label the y-axis
plt.grid(True)  # Add a grid for easier visualization
plt.show()  # Display the plot
