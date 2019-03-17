#Name: Marie Wothe
#Homework 3: Python Challenge: PyPoll

#Dependencies
import pandas as pd
import os

#Find and read the data from the resources folder
voting_file = os.path.join("Resources", "election_data.csv")

#Create data frame
vote = pd.read_csv(voting_file)
vote_df = pd.DataFrame(vote)

#The total number of votes cast
total = pd.DataFrame(vote_df.count())
total_votes = total.iloc[1,0]

#A complete number of candidates who received votes
candidates = vote_df["Candidate"].unique()

#The total number of votes each candidate won
counting_votes = vote_df["Candidate"].value_counts()
voter_count = pd.DataFrame(counting_votes)

#The percentage of votes each candidate won
percent = round(voter_count["Candidate"]/total_votes*100)
voter_count["Percent of Votes"] = percent

#The winner of the election based on popular vote
voter_count2 = voter_count.rename(columns = {"Candidate": "Number of Votes"})

#Re-order the columns
voter_count2 = voter_count2[["Percent of Votes", "Number of Votes"]]
voter_count3 = pd.DataFrame(voter_count2)

#need to un-index the candidate name 
final_data = voter_count3.reset_index()

#Final Formatting
final_data["Number of Votes"] = final_data["Number of Votes"].map("({:,})".format)
final_data["Percent of Votes"] = final_data["Percent of Votes"].map("{:.2f}%".format)

#Results
#Print to Terminal
print("Election Results")
print("---------------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------------")
print(final_data.to_string(header= ""))
print ("--------------------------")
print(" Winner: " + final_data.iloc[0,0])
print("----------------------------")

#Print Results to text file
text_file = open("PyPoll_results.txt", "w")
text_file.write("""Election Results
---------------------------
Total Votes: 3521001
-----------------------------
0      Khan  63.00%  (2,218,231)
1    Correy  20.00%    (704,200)
2        Li  14.00%    (492,940)
3  O'Tooley   3.00%    (105,630)
--------------------------
 Winner: Khan
----------------------------""")
text_file.close()