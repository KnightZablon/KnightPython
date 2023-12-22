import pandas as pd
import matplotlib.pyplot as plt

# Load data into a DataFrame
newCsvFile =  'C:\\Users\\knigh\\PycharmProjects\\knightpythonProject\\testD\\testD\\studentTestData.csv'
df = pd.read_csv(newCsvFile)

# Display a few rows of the DataFrame for inspection
print("DataFrame Preview:")
print(df.head())

# Example: Bar Plot
plt.figure(figsize=(10, 6))
plt.bar(df['Subject'], df['Score'], color='c')
plt.title('Bar Plot: Score by Subject')
plt.xlabel('Subject')
plt.ylabel('Score')
plt.grid(axis='y')
plt.show()
