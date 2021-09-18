import os
import csv



# Path to collect data from the Resources folder
election_data_csv = os.path.join('..', 'Resources', 'election_data.csv')

election_dictionary = {}

# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header_row = next(csvreader)
    
    #initialize variables which will be used in a subsquent loop to create a dictionary
    votes = 0
    vote_total = 0
    vote_pct = 0
    vote_winner = 0

# Dictionary creation Loop:  now create a dictionary of candidates, votes, and vote %.  
# I used a tuple for the vote stats in order to iterate and print the results later on
# ...i originally used a list but that didn't work in the Output Results Loop below (unhashable)
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        vote_total +=1

        # if a candidate is encountered for the first time, initialize his/her  vote total to 1 as he/she will be added to the dictionary for the first time
        # otherwise the candidate key already exists, and we increment his/her number of votes by 1
        if candidate not in election_dictionary:
            votes = 1
        else:
            votes = election_dictionary[candidate][0]+1

        # Next, calculate the cummulative vote percentage, and add the stats to the dictionary for the candidate
        vote_pct = votes/vote_total   
        election_dictionary[candidate] =(votes, vote_pct)

# create a "complete list of the candidates who received votes" as instructed in the homework
# not sure if this line is necessary to complete the homework
candidate_list = list(election_dictionary.keys())

# now output results to terminal
print("\n")
print("- - - - - - - - - - - - - - - -")
print("Election Results")
print("- - - - - - - - - - - - - - - -")
print(f"Total Votes: {vote_total}")
print("- - - - - - - - - - - - - - - -")

# initialize variables to be used in the Terminal Results Output Loop 
highest_votes=0
winner=[]

# Terminal Results Output Loop: this for loop pulls out the candidates and vote stats, and prints them to the terminal. 
for key,candidate in election_dictionary.items():

    candidate_percentage = "{:.3%}".format(candidate[1])
    candidate_votes = candidate[0]

    # Use conditionals to identify the candidiate with highest number of votes
    if candidate_votes > highest_votes:
        highest_votes=candidate_votes
        winner = key
    elif candidate_votes == highest_votes:
        highest_votes=candidate_votes
        winner.append(key)
    print(f"{key} : {candidate_percentage} ({candidate_votes})")

print("- - - - - - - - - - - - - - - -")
print(f"Winner: {winner.upper()} !!")
print("- - - - - - - - - - - - - - - -")



# now output result to text file.  This is pretty redundant but more or less
# the same code as above, inside a with open

pypoll_text_output = '../analysis/pypoll_text_output.txt'

with open (pypoll_text_output,'w') as text:

    
    text.write("- - - - - - - - - - - - - - - -\n")
    text.write("Election Results\n")
    text.write("- - - - - - - - - - - - - - - -\n")
    text.write(f"total votes: {vote_total}\n")
    text.write("- - - - - - - - - - - - - - - -\n")

    highest_votes=0
    winner=[]

    for key,candidate in election_dictionary.items():

        candidate_percentage = "{:.3%}".format(candidate[1])
        candidate_votes = candidate[0]
        if candidate_votes > highest_votes:
            highest_votes=candidate_votes
            winner = key
        elif candidate_votes == highest_votes:
            highest_votes=candidate_votes
            winner.append(key)
        text.write(f"{key} : {candidate_percentage} ({candidate_votes})\n")

    text.write("- - - - - - - - - - - - - - - -\n")
    text.write(f"Winner: {winner}\n")
    text.write("- - - - - - - - - - - - - - - -\n")