# Mason Dalton
# 003
# Description: Create a data frame with people, age, location, and Salary. Output, update, sort through the data frame

import pandas as pd

# create and assign dataframe of names
dfNames = pd.read_csv("HomeWork/PandasHW/practice_names.csv")

# Output all values in city column and then another with both name and age columns
print(dfNames["city"], end="\n\n")
print(dfNames[["name", "age"]], end="\n\n")

# Change the Salary of Joey Tribiani and age of Jane Smith. Then output data in row for both people
dfNames.at[8, "salary"] = 56000
dfNames.at[1, "age"] = 29
print(dfNames.loc[8], end="\n\n")
print(dfNames.loc[1], end="\n\n")

# Filter dataframe to include those older than 35 living in Seattle, Boston, San Francisco. Change dataframe and output it
dfNames = dfNames.query("(age > 35) and (city == 'Seattle' or city == 'Boston' or city == 'San Francisco')")
print(dfNames, end="\n\n")

# Sort remaining values by highest to lowest salary. Output adjusted dataframe
dfNames.sort_values('salary', ascending=False, inplace=True)
print(dfNames, end="\n\n")