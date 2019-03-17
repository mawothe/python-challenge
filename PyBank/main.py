#Name: Marie Wothe
#Homework 3: Python Challenge: PyBank

#Dependencies
import os
import pandas as pd

#Find and read data into data frame from Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")
budget_df = pd.read_csv(budget_csv)

#The total number of months included in the dataset
months_total = len(budget_df)
print(months_total)

#The net total amount "Profit/Losses" over the entire period
net_total = sum(budget_df["Profit/Losses"])

#new column with the difference between the current and previous month's p&l
change = budget_df["Profit/Losses"].diff()

#Add new column with the data
budget_df["Change in Profit/Losses"] = change
    
#The average (mean) of the changes in "Profit/Losses" over the entire period
average_delta = round(budget_df["Change in Profit/Losses"].mean(),2)

#The greatest increace in profits (date and amount) over the entire period
greatest_inc = budget_df["Change in Profit/Losses"].max()

#The greatest decrease in losses (date and amount) over the entire period
greatest_dec = budget_df["Change in Profit/Losses"].min()

#Results and Final Formatting
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(months_total))
print("Total: " + "$" + str(net_total))
print("Average Change: " + "$" + str(average_delta))
print("Greatest Increase in Profits: " + budget_df.iloc[25,0] +\
" ($" + str(greatest_inc) + ")")
print("Greatest Decrease in Profits: " + budget_df.iloc[44,0]+\
" ($" + str(greatest_dec) + ")")

#Print to text file
text_file = open("PyBANK_results.txt", "w")
text_file.write("""Financial Analysis
-----------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159.0)
Greatest Decrease in Profits: Sep-2013 ($-2196167.0)""")
text_file.close()