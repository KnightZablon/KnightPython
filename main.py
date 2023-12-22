import pandas as pd

def extract_data(csv_file_path):
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Print the first few rows of the DataFrame
    print("Extracted Data:")
    print(df.head())

    # Return the DataFrame if you want to use the data further in your application
    return df

if __name__ == "__main__":
    # file path for CSV file replace with your local drive path
    csv_file_path = 'C:\\Users\\knigh\\PycharmProjects\\knightpythonProject\\testD\\testD\\studentTestData.csv'

    # Call the function to extract data from the CSV file
    extracted_data = extract_data(csv_file_path)

    # You can now use 'extracted_data' for further processing or analysis

