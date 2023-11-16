# Modules
import os
import csv

# Prompt user for title lookup

# Set path for file
csvpath = r"PyPoll\Resources\election_data.csv"

# Initialize variables to store analysis results
total_votes = 0
candidates = {}  # Dictionary to store candidate names as keys and vote counts as values


# Open the CSV 
with open(csvpath, 'r') as csvfile:
      csvreader = csv.DictReader(csvfile)

      for row in csvreader:
        # Extract candidate name from the row
        candidate = row["Candidate"]

        # Update total number of votes
        total_votes += 1

        # Update vote count for the candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Analyze the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and display the results for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# Determine the winner based on popular vote
winner = max(candidates, key=candidates.get)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save the results to a text file
output_file_path = r"PyPoll\analysis\election_results.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

print(f"Results saved to {output_file_path}")