# The data we need tor etrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recived votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
# Add dependencies
#import csv

#import os

 # Assign a variable to file path

#file_to_load = 'Resources/election_results.csv'

# Assing a variable to save the file to a path.
#file_to_save= 'analysis/election_analysis.txt'

 # Open the election results and read the file.

#with open(file_to_load) as election_data:

    # Print the file object
    #print(election_data)
  
# To do: perform analysis
    
# close the file
#election_data.close()

# Create a filename variable to a direct or indirect path to file.

#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.

#open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.

#file_to_save = os.path.join("analysis", "election_analysis.txt")


# Use the open statement to open the file as a text file.

#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.

    #txt_file.write("Hello World")

    # Write three counties to the file.
    # Line by line example below
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # New line escape sequence 
    #txt_file.write("Counties in the Election\n--------------\n")
    
    #txt_file.write("Arapahoe\nDenver\nJefferson")
    
# Close the file

#txt_file.close()

# Add our dependencies.

#import csv

#import os

# Assign a variable to load a file from the path

#file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.

#file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
#total_votes = 0

# Candidate options
#candidate_options = []
# Open the election results and read the file.
#with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    #file_reader = csv.reader(election_data)

    # Read the header row.
    #headers= next(file_reader)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
    
    # Read the file object with the reader function.
    #file_reader = csv.reader(election_data)
    # Print the header row
    #   print(headers)
    # Print each row in the CSV file.
    #for row in file_reader:
        # 2. Add to the total vote count.
        #total_votes += 1
# 3. Print the total votes.
    #print(total_votes)
# Print the candidate name from each row
    #candidate_name = row[2]
    # If the candidate name from each row.
    #if candidate_name not in candidate_options:
        # Add it to the list of candidates.
        #candidate_options.append(candidate_name)

    # Add the candidate name to the candidate list.
    #candidate_options.append(candidate_name)
# Print the candidate list.
#print(candidate_options)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)








    


