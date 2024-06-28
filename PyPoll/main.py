# Dependecies
import os
import csv
import pathlib

# Set the path for the CSV file
# https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
current_path = pathlib.Path(__file__).parent.resolve()
csvpath = os.path.join(current_path, 'Resources', 'election_data.csv')
analysispath = os.path.join(current_path, 'Analysis')

# Open the CSV file
with open(csvpath) as csvfile:
    csvfile_read = csv.reader(csvfile, delimiter=',')
    header = next(csvfile_read)

    # Declare all the variables/counters
    vote_count = 0
    candidates = []
    candidates_votes = []
    
    
    # Looping through the CSV file
    for row in csvfile_read:
            vote_count += 1

            # Adding every candidate with at least one vote
            if row[2] not in candidates:
                  candidates.append(row[2])
            
            # Determine which candidate gets the vote
            for i in candidates:
                  if row[2] == candidates[i]:
                        candidates_votes[i] += 1


print(candidates)
print(candidates_votes)

# Print the Financial Analysis
print("\nElection Results\n----------------------------")
print("Total Votes", vote_count, "\n----------------------------")

# # Create a txt file with the analysis
# pathlib.Path(os.path.join(analysispath, "results.txt")).touch()
# with open(os.path.join(analysispath, "results.txt"), "w") as f:
#     f.write("Election Results\n----------------------------")
