# Election_Analysis
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

- 
