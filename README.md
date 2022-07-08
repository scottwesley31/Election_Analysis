# Election Analysis
Module 3 Python

Note: The following section was copied from Module 3; Deliverable 3 starts at "Challenge Overview".
## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total  number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.68.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette who received 73.8% of the vote and 272,892 number of votes.

## Challenge Overview

Seth and Tom (Colorado Board of Education employees) requested additional information from the audit to submit to the election commision. The commission has requested the following information:

1. The voter turnout for each county
2. The percentage of votes for each county out of the total count
3. The county with the highest turnout

## Challenge Summary
### Election-Audit Results:
- A total of 369,711 votes were cast in this congressional election. This value was calculated by having the code read the election_results.csv file, skipping over the head, initializing a "total_votes" variable to zero, and incrementing this variable by 1 for every row.

![image](https://user-images.githubusercontent.com/107309793/177759468-7730311f-91af-47ad-8d13-9d050105aa40.png)

This value was later printed to a text file called "election_analysis.txt".

![total_votes_2](https://user-images.githubusercontent.com/107309793/177760240-a052554a-8a03-4cad-9d3c-77a092739387.png)

This is the print statement code:

![total_votes_3](https://user-images.githubusercontent.com/107309793/177760419-ead2e80e-f36e-4ad5-a7aa-24b8a846a99c.png)

- The vote count and percentage of the total vote for each county is as follows:
  - Jefferson - 38,855 (10.5%)
  - Denver - 306,055 (82.8%)
  - Arapahoe - 24,801 (6.7%)
  
This was accomplished by creating an empty county list and county votes dictionary as follows:

![county_results](https://user-images.githubusercontent.com/107309793/177763389-c0dcd842-cb33-4dcc-8eab-c30edc84597b.png)

A conditional statement was utilized within the `For row in reader:` for loop screenshotted above (which references the election_results.csv) which appends the unique county names from the file to a list and generating a vote count by initializing the count to zero and incrementing by 1. This is done for each county. This is executed in the following code.
 
  ![county_results_2](https://user-images.githubusercontent.com/107309793/177764654-0404fdfa-cebf-46c3-8f78-f190a3132d06.png)
  
The variable `county_name` was defined prior to this if statement and contains the county names from the election_results.csv file.
  
At this point the county list is populated with the counties from the election_results.csv file (Jefferson, Denver, Arapahoe) and the county votes dictionary is populated with the total vote count for each county.

The county votes dictionary is accessed in another for loop which retrives the vote count and assigns it to a variable `vote_county_count`, and uses this value and the `total_votes` variable to calculate the percentage of votes `vote_county_percent`.

![county_results_3](https://user-images.githubusercontent.com/107309793/177765715-421c3fd4-b6d8-4214-9e59-a9386238c48d.png)

This is then printed in a similar fashion to the election results to the terminal (and the election_analysis.txt text file).

![county_results_5](https://user-images.githubusercontent.com/107309793/177766547-1d16a08f-9cb7-415b-a04f-b0c78d2a5cfb.png)

This is the print statement code:

![county_results_4](https://user-images.githubusercontent.com/107309793/177765869-7062320e-494a-4119-a08f-716bb514d8c1.png)

- The county that had the largest number of votes was Denver. This was accomplished by utilizing the same `for county in county_dict.keys()` for loop from before which references the `county_dict` dictionary containing the counties and their associated vote counts.

2 empty variables were defined prior to using this loop which will later be populated with the winning county and it's number of votes.

![winning_county](https://user-images.githubusercontent.com/107309793/177767863-46b03d59-84b1-4b05-b3ac-bcc99a7373d9.png)

A conditional statement within the for loop checks for when `vote_county_county > winning_votes`. While iterating through the `county_dict` dictionary, the code finds each county vote `vote_county_count` and checks to see if it is larger than the `winning_votes` variable (which starts at zero). Each time the for loop satisfies this condition, the `winning_county` string is updated with that county and the `winning_votes` is updated to the dictionary value with the highest count. Here's the code:

![winning_county_2](https://user-images.githubusercontent.com/107309793/177769154-8bfd03f7-2d29-465e-b421-3261c5e96c58.png)

A largest turnout summary is printed underneath the county details into the election_analysis.txt file. Note: a candidate results print statement was added here preemptively before the code for the candidate results section. This was simply done here to indicate the start of the candidate results data in the election_analysis.txt file.

![winning_county_4](https://user-images.githubusercontent.com/107309793/177770596-ecceb625-a70a-42ce-9327-de89fb02851f.png)

![winning_county_3](https://user-images.githubusercontent.com/107309793/177770427-7d8e0d37-27f4-458a-824b-e9b754de2ef4.png)

- There were 3 different candidates in this election - Charles Casper Stockham, who received 23.0% of the votes (85,213 votes), Diana DeGette, who received 73.8% of the votes (272,892), and Raymon Anthony, who received 3.1% of the votes (11,606). These values were obtained in a very similar fashion to the vote counts and vote percentages that were associated with each county.

An empty candidate options list and candidates votes dictionary was created.

![candidate_results](https://user-images.githubusercontent.com/107309793/177889753-7df51d00-a0ee-4915-837c-b4fcb0bdd616.png)

A conditional statement was utilized within the `For row in reader:` for loop which appends the unique candidate names from the election_results.csv file to a list and generates a vote count. The vote count is initiated to zero and incremented by 1.

![candidate_results_2](https://user-images.githubusercontent.com/107309793/177891156-0c52a018-8f37-4a4d-9fcf-be2751f5cea5.png)

The `candidate_name` variable was defined first in this loop and contains the candidate names extracted from the election_results.csv file.

[]At this point the county list is populated with the counties from the election_results.csv file (Jefferson, Denver, Arapahoe) and the county votes dictionary is populated with the total vote count for each county.

[]The county votes dictionary is accessed in another for loop which retrives the vote count and assigns it to a variable `vote_county_count`, and uses this value and the `total_votes` variable to calculate the percentage of votes `vote_county_percent`.

[]This is then printed in a similar fashion to the election results to the terminal (and the election_analysis.txt text file).

[]This is the print statement code:
