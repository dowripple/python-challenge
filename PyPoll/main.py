import os
import csv

# Path to collect data from the Resources folder
poll_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(poll_csv, 'r') as csvfile:

    #setup the reader 
    csvreader = csv.reader(csvfile)
    
    #grab the header, skip to next row
    header = next(csvreader)

    #variable for counting total votes
    totalVotes = 0

    #list of candidates
    candidates = []

    #looping through reader
    for row in csvreader:

        #if the candidate for this row has not been added to the list of dictionaries, do so
        if not any(candidate["name"] == row[2] for candidate in candidates):
            candidates.append({"name": row[2], "votes": 0})

        #loop through candidates, if match to row, increment vote count for candidate
        for candidate in candidates:

            if candidate["name"] == row[2]:
                candidate["votes"] += 1
        
        #increment vote counter
        totalVotes += 1

    #start printing the results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {totalVotes}")
    print("-------------------------")
    
    #variable to store the winner
    winnerVotes = 0
    winnerName = ""

    #loop through candidates, printing one line for each
    for candidate in candidates:

        #calc that candidates percentage of vote
        percentVote = round((candidate["votes"] / totalVotes) * 100,3)

        #see if he/she is a winner
        if candidate["votes"] > winnerVotes:
            winnerVotes = candidate["votes"]
            winnerName = candidate["name"]

        #print out the candidate line
        print(f'{candidate["name"]}: {percentVote}%  ({candidate["votes"]})')

    #print out the winner
    print("-------------------------")
    print(f'Winner: {winnerName}')
    print("-------------------------")

    #create the results file
    with open("results.txt", 'w') as resultFile:

        #write the same information to the new file, adding \n for new line    
        resultFile.write("Election Results\n")
        resultFile.write("-------------------------\n")
        resultFile.write(f"Total Votes: {totalVotes}\n")
        resultFile.write("-------------------------\n")

        #loop through candidates again to print the results    
        for candidate in candidates:

            #calc the percentage again
            percentVote = round((candidate["votes"] / totalVotes) * 100,3)

            #write the candidate line
            resultFile.write(f'{candidate["name"]}: {percentVote}%  ({candidate["votes"]})\n')

        #write out the winner
        resultFile.write("-------------------------\n")
        resultFile.write(f'Winner: {winnerName}\n')
        resultFile.write("-------------------------\n")
