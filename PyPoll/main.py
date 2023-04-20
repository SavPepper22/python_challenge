#First I need to import the csv library and module I will use.

import os
import csv

#Need to make an object using the name of the class I want to use the variables and values.
election_data = os.path.join("election_data.csv")

#Make empty lists so the csv values can be added.
candidate = []
number_votes = []
candidate_vote = {}
total_votes = 0

#Open and read the csv file.
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile)

    #Extract the field names and make a header.
    csv_header = next(csvreader)

    #Go through each row of data.
    for row in csvreader:
      
        #Review and categorize the values and then add them to the lists.
        #for row in csvreader:
        total_votes += 1
            
            #Make a conditional statment that will tally votes based on the name of the candidate.
            #make a list of candidates

        candidate_name = row[2]
        if candidate_name not in candidate: 
            candidate.append(candidate_name)
            candidate_vote[candidate_name] = 0

        candidate_vote[candidate_name] += 1
        number_votes.append(row[1])
        
#Displaying Results
print("Election Results")
print("---------------------")
#Print total number of votes.
print(f"Total Votes : {str(total_votes)}")
print("---------------------")
#print results of candidate and number of votes with percentage.         
#print(candidate)
#print(candidate_vote)
for candidate, votes in candidate_vote.items():
    print(candidate + ":" + "{:.3%}". format(votes/total_votes) + " (" + str(votes) + ")")

print("---------------------")
#Write out a code to find the winner and print it.
winner = max(candidate_vote, key = candidate_vote.get)
print(f"Winner: {winner}")

#Now make a new text file and print our results.

f = open("election_results.txt", "w")
f.write("Election Results")
f.write("\n")
f.write("---------------------")
f.write("\n")
f.write(f"Total Votes : {str(total_votes)}")
f.write("\n")
f.write("---------------------")
f.write("\n")
    
for candidate, votes in candidate_vote.items():
    f.write(candidate + ":" + "{:.3%}". format(votes/total_votes) + " (" + str(votes) + ")")
    f.write("\n")
f.write("---------------------")
f.write("\n")
winner = max(candidate_vote, key = candidate_vote.get)
f.write(f"Winner: {winner}")
f.write("\n")
f.write("---------------------")