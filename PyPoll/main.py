# Modules
import os
import csv

# Prompt user for title lookup

# Set path for file
csvpath = r"PyPoll\Resources\election_data.csv"
# Set variable to check if we found the video

# Open the CSV using the UTF-8 encoding
with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header_row= next(csvreader)
        print(header_row)