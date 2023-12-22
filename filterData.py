import pandas as pd

# Load data into a DataFrame
df = pd.read_csv('C:\\Users\\knigh\\PycharmProjects\\knightpythonProject\\testD\\testD\\studentTestData.csv')

# Group by 'StudentID' and calculate the mean of 'Score' for each student
grouped_data = df.groupby('StudentID')['Score'].mean()

# Convert the grouped data (Series) to a DataFrame
result_df = grouped_data.reset_index(name='MeanScore')

# Display the resulting DataFrame with mean scores
print("\nMean Scores:")
print(result_df)
newCsvFile = 'C:\\Users\\knigh\\PycharmProjects\\knightpythonProject\\testD\\testD\\newStudentTestData.csv'
# Write the grouped data to a new CSV file
result_df.to_csv(newCsvFile, index=False)

