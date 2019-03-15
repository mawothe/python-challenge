#Dependencies
import os
import numpy
import pandas as pd

#Find and read the data from the resources folder
voting_file = os.path.join("Resources", "election_data.csv")

#Create data frame
vote_df = pd.read_csv(voting_file)
vote_df.head()

#The total number of votes cast
total_votes = vote_df.describe

#A complete number of candidates who received votes
candidates = vote_df("candidate").unique()

#The percentage of votes each candidate won


#The total number of votes each candidate won
counting_votes = vote_df("candidate").value_counts()

#The winner of the election based on popular vote


#Results
print("Election Results")
print("---------------------------")
print("Total Votes: " + total_votes)
print(" Person 1 ...")
print(" Person 2...")
print(" Person 3...")
print ("--------------------------")
print(" Winner: " + )
print("----------------------------")

#can you make the results of a calculation done on a data frame 
#into an new data frame? 
#can you use the data to make a new table of the data? (a variant of the prev. q.?)