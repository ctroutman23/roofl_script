import pandas as pd


# This script automates the process for taking lead info from roofl and 
# cleaning/manipulating it to use for mail merge labels to be printed

# Read in roofl lead csv
roofl_df = pd.read_csv("data/leads-2-13-2025.csv")

# remove whitespace from column names
roofl_df.columns = roofl_df.columns.str.replace(' ', '_')
# print(roofl_df.columns)

# remove irrelevant info from "Contact_Name" column 
roofl_df = roofl_df.query("Status == 'Open'")

# Remove ", USA" from Address column
roofl_df['Address'] = roofl_df['Address'].str.replace(", USA", "", regex=False)


# change dataframe to only include the "Contact_Name" and "Address" columns
relevant_columns = ['Contact_Name', 'Address']
roofl_df = roofl_df[relevant_columns]
print(roofl_df)

# Write updated df to new csv file to be used for mail merge
roofl_df.to_csv('data/cleaned_roofl.csv', index=False)