#PyPoll python code

#import functions that will be used
import os
import csv

#Collect data from csv in Resources folder & set output file
polldata = os.path.join('Resources', 'election_data.csv')
polloutput = os.path.join('analysis', 'poll_output.txt')

#Set lists and variables to analyse data
totalvotes = 0
candidates = []
candidatevotes = {} #Dictionary to track votes per candidate (candidates are the keys)
winner = ""
winnervotes = 0

#read in the data from csv file
with open(polldata, 'r') as csvfile:

    #Using dictreader for superior code readability
    csvreader = csv.DictReader(csvfile, delimiter=',')

    #Read all rows in the CSV file to gather desired data
    for row in csvreader:
        
        #Total vote count is incremented for every row (for percentage calculation)
        totalvotes += 1

        #Obtain the condidate name for this row
        currentcandidate = row["Candidate"]

        #If the candidate of this row is a new candidate observed (does does not match an existing candidate)
        if currentcandidate not in candidates:

            #Add this new candidate to the list of total candidates
            candidates.append(currentcandidate)

            #Initialise tracking for new candidates votes (create new key)
            candidatevotes[currentcandidate] = 0
        
        #Add a vote for current candidate
        candidatevotes[currentcandidate] += 1

    #print(totalvotes)
    #print(candidates)
    #print(candidatevotes)

#Write the analysis to file as we calculate (else we would have to store output data somewhere)
with open(polloutput, 'w') as outputfile:

    #Print the title and total votes to terminal
    print("Election Results")
    print("--------------------------")
    print("Total Votes: " + str(totalvotes))
    print("--------------------------")
    #Write the title and total votes to file
    outputfile.write("Election Results\n")
    outputfile.write("--------------------------\n")
    outputfile.write("Total Votes: " + str(totalvotes) + "\n")
    outputfile.write("--------------------------\n")

    #Cycle through entire dictionary to print results for each candidate
    for candidate in candidatevotes:

        #Extract votes for current candidate in dictionary
        votes = candidatevotes.get(candidate)
        #Calculate percentage of votes for this candidate
        voteperc = round((float(votes)/float(totalvotes)) * 100, 3)

        #Check if current candidate has most votes so far (winnervotes inititalised as 0)
        if votes > winnervotes:
            #If so, set new winner stats
            winnervotes = votes
            winner = candidate

        #Print data for this candidate and write to file
        print(candidate + ": " + str(voteperc) + "% (" + str(votes) + ")")
        outputfile.write(candidate + ": " + str(voteperc) + "% (" + str(votes) + ")\n")
    
    #After winner has been determined, print and write to file
    print("--------------------------")
    print("Winner: " + winner)
    print("--------------------------")
    outputfile.write("--------------------------")
    outputfile.write("Winner: " + winner)
    outputfile.write("--------------------------")
    