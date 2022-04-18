# The data we need tor etrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recived votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
# Add dependencies
import csv

import os

 # Assign a variable to file path

file_to_load = 'Resources/election_results.csv'
 # Open the election results and read the file.

with open(file_to_load) as election_data:

    # Print the file object
    print(election_data)
  
# To do: perform analysis
    
# close the file
election_data.close()

# Create a filename variable to a direct or indirect path to file.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.

open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.

file_to_save = os.path.join("analysis", "election_analysis.txt")


# Use the open statement to open the file as a text file.

with open(file_to_save, "w") as txt_file:

    # Write some data to the file.

    #txt_file.write("Hello World")

    # Write three counties to the file.
    # Line by line example below
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # New line escape sequence 
    txt_file.write("Counties in the Election\n--------------\n")
    
    txt_file.write("Arapahoe\nDenver\nJefferson")
    
# Close the file

txt_file.close()

# Add our dependencies.

import csv

import os

# Assign a variable to load a file from the path

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.

file_to_save = os.path.join("Resources", "election_analysis.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    
    file_reader=csv.reader(election_data)

    # Print each row in the CSV file.
    
    for row in file_reader:
        print(row)
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)
    


