# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# # Assign a variable for the file to load the path.
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     #To do: perform analysis.
#     print(election_data)
# # Close the file.

# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources","election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     # Print the file object
#     print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# #Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
#     # Write some data to the file.
#     # txt_file.write("Hello World")

#     # # Write three counties to the file.
#     # txt_file.write("Arapahoe, ")
#     # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson, ")

#     # # Write three counties to the file.
#     # txt_file.write("Arapahoe, Denver, Jefferson")

#     # # Write three counties to the file.
#     # txt_file.write("Arapahoe\nDenver\nJefferson")

#     # Skill Drill
#     txt_file.write("Counties in the Election\n" + "-" *24 + "-\nArapahoe\nDenver\nJefferson")

####################################
# 3.4.4: READ THE ELECTION RESULTS #
####################################

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Declare candidate options list.
candidate_options = []

# Declare an empty dictionary for candidate votes.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
   
    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    #############################
    # 3.5.1 GET THE TOTAL VOTES #
    #############################

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

    # # Print the total votes.
    # print(total_votes)

############################################
# 3.5.2 GET THE CANDIDATES IN THE ELECTION #
############################################

        # Print the candidate name for each row
        candidate_name = row[2]

        # # Add the candidate name to the candidate list.
        # candidate_options.append(candidate_name)

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

# # Print the candidate list.
# print(candidate_options)

###################################
# 3.5.3 GET THE CANDIDATES' VOTES #
###################################
            
            # Begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# # Print the candidate vote dictionary.
# print(candidate_votes)

#####################################################
# 3.5.4 DETERMINING CANDIDATES' PERCENTAGE OF VOTES #
#####################################################

# Determine the percentage of votes for each candidate by looping through the counts.

# Interate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of candidate.
    votes = candidate_votes[candidate_name]
    
    # Calculate the percentage of votes.
    vote_percentage = float(votes)/float(total_votes) * 100

    # # Print the candidate name and percentage of votes.
    # # SKill Drill: f'{value:{width}.{precision}}' f'{value:.1f} will print only to 1 decimal place
    # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

#########################################
# 3.5.5 DETERMINE THE WINNING CANDIDATE #
#########################################

    # Determine winning vote count and candidate

    # Print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning percent = vote percentage.
        winning_count = votes
        winning_percentage = vote_percentage

        # Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n"
)

print(winning_candidate_summary)