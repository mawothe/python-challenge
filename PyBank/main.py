#Dependencies
import os
import pandas as pd

#Find and read data into data frame from Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")
budget_df = pd.read_csv(budget_csv)

#The total number of months included in the dataset

#The net total amount "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increace in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

#Results
print("Financial Analysis")
print(" ")
print("_______________________________")
print("Total Months: " + )
print("Total: " + )
print("Average Change: " + )
print("Greatest Increase in Profits: " + )
print("Greatest Decrease in Profits: " +)