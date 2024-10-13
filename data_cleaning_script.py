
# import pandas as pd

# # If your data starts after metadata rows, skip them (e.g., skiprows=4 skips the first 4 lines)
# df = pd.read_csv("/Users/ekramulislam/Documents/DataVisFIT3179/FIT3179Visualization2/Data/API_EG.FEC.RNEW.ZS_DS2_en_csv_v2_1722.csv", skiprows=4)

# # Preview the first few rows to verify if it's correctly loaded
# print(df.head())

# import pandas as pd

# # Step 1: Load the CSV file (you can replace this with your actual file path)
# df = pd.read_csv('/Users/ekramulislam/Documents/DataVisFIT3179/FIT3179Visualization2/Data/API_EG.FEC.RNEW.ZS_DS2_en_csv_v2_1722.csv', skiprows=4)

# # Step 2: Remove the "Unnamed: 68" column if it contains only NaN values
# df = df.drop(columns=['Unnamed: 68'], errors='ignore')

# # Step 3: Drop any rows that are completely empty (all NaN values)
# df_cleaned = df.dropna(how='all')

# # Step 4: Handle missing values for specific columns (years) if needed
# # You can choose to drop rows where key columns (e.g., 2020, 2021) have NaN values, or fill them
# df_cleaned = df_cleaned.dropna(subset=['2020', '2021'])  # Drops rows with NaN in important columns

# # Alternatively, fill missing values with 0 or column mean
# # df_cleaned = df_cleaned.fillna(0)  # Fill NaN with 0
# # df_cleaned = df_cleaned.fillna(df_cleaned.mean())  # Fill NaN with column mean

# # Step 5: Preview the cleaned data
# print(df_cleaned.head())

# # Step 6: Save the cleaned data to a new CSV file
# df_cleaned.to_csv('cleaned_data.csv', index=False)

# print("Data cleaning complete. Cleaned data saved to 'cleaned_data.csv'.")


# import pandas as pd

# # Step 1: Load your CSV data
# # Replace 'your_data.csv' with the actual file path of your data
# df = pd.read_csv('/Users/ekramulislam/Documents/DataVisFIT3179/FIT3179Visualization2/Data/API_EG.FEC.RNEW.ZS_DS2_en_csv_v2_1722.csv')

# # Step 2: Display the first few rows of the dataset to inspect it
# print("Initial Data Preview:")
# print(df.head())

# # Step 3: Check for null values
# print("\nSummary of Null Values in Each Column:")
# print(df.isnull().sum())

# # Step 4: Drop rows where **all** values are null (completely blank rows)
# df_cleaned = df.dropna(how='all')

# # Step 5: Drop rows with any null values in **important columns**
# # Replace 'important_column' with the column name(s) you want to clean specifically
# df_cleaned = df_cleaned.dropna(subset=['important_column'])

# # Step 6: (Optional) Drop columns if they have more than a certain percentage of null values
# # Here, we drop columns that are more than 50% null values
# threshold = 0.5 * len(df_cleaned)
# df_cleaned = df_cleaned.dropna(axis=1, thresh=threshold)

# # Step 7: Display cleaned data and check again for null values
# print("\nCleaned Data Preview:")
# print(df_cleaned.head())

# print("\nSummary of Null Values After Cleaning:")
# print(df_cleaned.isnull().sum())

# # Step 8: Save the cleaned data to a new CSV file
# df_cleaned.to_csv('cleaned_data.csv', index=False)

# print("\nData cleaning complete. Cleaned data saved to 'cleaned_data.csv'.")


# import pandas as pd

# # Step 1: Load the CSV file, skipping the first 4 metadata rows
# df = pd.read_csv('/Users/ekramulislam/Documents/DataVisFIT3179/FIT3179Visualization2/Data/API_EG.FEC.RNEW.ZS_DS2_en_csv_v2_1722.csv', skiprows=4)

# # Step 2: Drop any columns that are not necessary (like Unnamed or extra empty columns)
# df = df.drop(columns=[col for col in df.columns if "Unnamed" in col], errors='ignore')

# # Step 3: Inspect the data to understand its structure
# print("First few rows of the dataset:")
# print(df.head())

# # Step 4: Remove rows where all columns are NaN (completely empty rows)
# df_cleaned = df.dropna(how='all')

# # Step 5: Optionally, drop rows where important columns (e.g., 2020, 2021) are NaN
# df_cleaned = df_cleaned.dropna(subset=['2020', '2021'])

# # Step 6: Save the cleaned data to a new file
# df_cleaned.to_csv('cleaned_data.csv', index=False)

# print("Data cleaning complete. Cleaned data saved to 'cleaned_data.csv'.")








# import pandas as pd

# # Step 1: Load your CSV file (adjust the file path as needed)
# df = pd.read_csv('/Users/ekramulislam/Documents/DataVisFIT3179/FIT3179Visualization2/Data/API_EG_FEC_RNEW_ZS_DS2_en_csv_v2_1722.csv', skiprows=4)

# # Step 2: Drop any "Unnamed" or extra columns if needed
# df = df.drop(columns=[col for col in df.columns if "Unnamed" in col], errors='ignore')

# # Step 3: Drop rows that are completely empty (all values are NaN)
# df_cleaned = df.dropna(how='all')

# # Step 4: Preview the cleaned data
# print("Cleaned Data Preview (first 5 rows):")
# print(df_cleaned.head())

# # Step 5: Save the cleaned data to a new CSV file
# df_cleaned.to_csv('cleaned_data_no_blanks.csv', index=False)

# print("Blank rows removed and cleaned data saved to 'cleaned_data_no_blanks.csv'.")















# import pandas as pd

# # Step 1: Load the CSV file (adjust the file path as needed)
# df = pd.read_csv('/Users/ekramulislam/Documents/DataVisFIT3179/FIT3179Visualization2/cleaned_data.csv', skiprows=4)

# # Step 2: Drop any "Unnamed" or extra columns if needed
# df = df.drop(columns=[col for col in df.columns if "Unnamed" in col], errors='ignore')

# # Step 3: Replace all NaN values with 0
# df_filled = df.fillna(0)

# # Step 4: Preview the cleaned data
# print("Data after replacing NaN values with 0 (first 5 rows):")
# print(df_filled.head())

# # Step 5: Save the modified data to a new CSV file
# df_filled.to_csv('data_no_nan_values.csv', index=False)

# print("NaN values replaced with 0 and saved to 'data_no_nan_values.csv'.")


# import pandas as pd

# # Step 1: Load the CSV file (adjust the file path as needed)
# df = pd.read_csv('/Users/ekramulislam/Documents/DataVisFIT3179/FIT3179Visualization2/cleaned_data.csv')

# # Step 2: Melt the DataFrame to shift year columns into a single 'Year' column
# # Assume the columns 'Country Name', 'Country Code', 'Indicator Name', and 'Indicator Code' are fixed
# df_melted = pd.melt(df, id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
#                     var_name='Year', value_name='Renewable_Energy_Consumption')

# # Step 3: Convert 'Year' to an integer (if needed)
# df_melted['Year'] = df_melted['Year'].astype(int)

# # Step 4: Preview the transformed data
# print("Transformed Data Preview (first 5 rows):")
# print(df_melted.head())

# # Step 5: Save the transformed data to a new CSV file
# df_melted.to_csv('transformed_data.csv', index=False)

# print("Data successfully transformed. Saved to 'transformed_data.csv'.")






# import pandas as pd

# # Step 1: Load the transformed CSV file (adjust the file path as needed)
# df = pd.read_csv('/Users/ekramulislam/Documents/DataVisFIT3179/FIT3179Visualization2/transformed_data.csv')

# # Step 2: Replace all NaN or missing values with 0
# df_filled = df.fillna(0)

# # Step 3: Preview the modified data
# print("Data after replacing missing values with 0 (first 5 rows):")
# print(df_filled.head())

# # Step 4: Save the cleaned data to a new CSV file
# df_filled.to_csv('filled_transformed_data.csv', index=False)

# print("Missing values replaced with 0 and saved to 'filled_transformed_data.csv'.")




# import pandas as pd

# # Step 1: Load the transformed CSV file (adjust the file path as needed)
# df = pd.read_csv('/Users/ekramulislam/Documents/DataVisFIT3179/FIT3179Visualization2/Data/Metadata_Country_API_EG.FEC.RNEW.ZS_DS2_en_csv_v2_1722.csv')






# # Step 2: Replace empty strings or whitespace cells with NaN
# df.replace(r'^\s*$', float('NaN'), regex=True, inplace=True)

# # Step 3: Drop rows where any value is NaN (remove rows with NaN values)
# df_cleaned = df.dropna(how='any')

# # Step 4: Preview the cleaned data
# print("Data after replacing empty cells with NaN and removing rows (first 5 rows):")
# print(df_cleaned.head())

# # Step 5: Save the cleaned data to a new CSV file
# df_cleaned.to_csv('final_data_no_empty_rows.csv', index=False)

# print("Empty cells replaced with NaN, rows with NaN removed, and cleaned data saved to 'final_data_no_empty_rows.csv'.")




# #data cleaning done for 2 of the datas present 



#to find the min and max value of the renewable energy consumption

import pandas as pd

# Load your CSV file
df = pd.read_csv('/Users/ekramulislam/Documents/DataVisFIT3179/FIT3179Visualization2/Data/API_EG_FEC_RNEW_ZS_DS2_en_csv_v2_1722.csv')

# Check the min and max of Renewable Energy Consumption
min_value = df['Renewable_Energy_Consumption'].min()
max_value = df['Renewable_Energy_Consumption'].max()

print(f"Min: {min_value}, Max: {max_value}")
