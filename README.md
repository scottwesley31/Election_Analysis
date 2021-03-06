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

#### Total Votes
A total of 369,711 votes were cast in this congressional election. This value was calculated by having the code read the election_results.csv file, skipping over the header, initializing a `total_votes` variable to zero, and incrementing this variable by 1 for every row.

![image](https://user-images.githubusercontent.com/107309793/177759468-7730311f-91af-47ad-8d13-9d050105aa40.png)

This value was later printed to a text file called "election_analysis.txt".

![total_votes_2](https://user-images.githubusercontent.com/107309793/177760240-a052554a-8a03-4cad-9d3c-77a092739387.png)

This is the print statement code:

![total_votes_3](https://user-images.githubusercontent.com/107309793/177760419-ead2e80e-f36e-4ad5-a7aa-24b8a846a99c.png)

#### Vote Count & Percentage of Total by County
The vote count and percentage of the total vote for each county is as follows:
  - **Jefferson - 38,855 (10.5%)**
  - **Denver - 306,055 (82.8%)**
  - **Arapahoe - 24,801 (6.7%)**
  
This was accomplished by creating an empty county list and county votes dictionary as follows:

![county_results](https://user-images.githubusercontent.com/107309793/177763389-c0dcd842-cb33-4dcc-8eab-c30edc84597b.png)

A conditional statement was utilized within the `For row in reader:` for loop screenshotted above (references the election_results.csv). It appends the unique county names from the file to a list and also generates a vote count by initializing the count to zero and incrementing by 1. This is done for each county and executed in the following code.
 
  ![county_results_2](https://user-images.githubusercontent.com/107309793/177764654-0404fdfa-cebf-46c3-8f78-f190a3132d06.png)
  
The variable `county_name` was defined prior to this if statement and contains the county names from the election_results.csv file.
  
At this point the county list is populated with the counties from the election_results.csv file (Jefferson, Denver, Arapahoe) and the county votes dictionary is populated with the total vote count for each county.

The county votes dictionary is accessed in another for loop which retrieves the vote count and assigns it to a variable (`vote_county_count`), and uses this value and the `total_votes` variable to calculate the percentage of votes (`vote_county_percent`).

![county_results_3](https://user-images.githubusercontent.com/107309793/177765715-421c3fd4-b6d8-4214-9e59-a9386238c48d.png)

This is then printed in a similar fashion to the election results to the terminal (and the election_analysis.txt text file).

![county_results_5](https://user-images.githubusercontent.com/107309793/177766547-1d16a08f-9cb7-415b-a04f-b0c78d2a5cfb.png)

This is the print statement code:

![county_results_4](https://user-images.githubusercontent.com/107309793/177765869-7062320e-494a-4119-a08f-716bb514d8c1.png)

#### Largest Vote Count by County

The county that had the largest number of votes was **Denver**. This was accomplished by utilizing the same `for county in county_dict.keys()` for loop from before which references the `county_dict` dictionary containing the counties and their associated vote counts.

2 empty variables were defined prior to using this loop which will later be populated with the winning county and it's number of votes.

![winning_county](https://user-images.githubusercontent.com/107309793/177767863-46b03d59-84b1-4b05-b3ac-bcc99a7373d9.png)

A conditional statement within the for loop checks for when `vote_county_county > winning_votes`. While iterating through the `county_dict` dictionary, the code finds each county vote (`vote_county_count`) and checks to see if it is larger than the `winning_votes` variable (which starts at zero). Each time the for loop satisfies this condition, the `winning_county` string is updated with that county and the `winning_votes` is updated to the dictionary value with the highest count. Here's the code:

![winning_county_2](https://user-images.githubusercontent.com/107309793/177769154-8bfd03f7-2d29-465e-b421-3261c5e96c58.png)

A largest turnout summary is printed underneath the county details into the election_analysis.txt file. Note: a candidate results print statement was added here preemptively before the code for the candidate results section. This was simply done here to indicate the start of the candidate results data in the election_analysis.txt file.

![winning_county_4](https://user-images.githubusercontent.com/107309793/177770596-ecceb625-a70a-42ce-9327-de89fb02851f.png)

![winning_county_3](https://user-images.githubusercontent.com/107309793/177770427-7d8e0d37-27f4-458a-824b-e9b754de2ef4.png)

#### Vote Count & Percentage of Total by Candidate

The candidate results were as follows:
- **Charles Casper Stockham had 23.0% of the total vote (85,213 votes)**
- **Diana DeGette had 73.8% of the total vote (272,892)**
- **Raymon Anthony Doane had 3.1% of the total vote (11,606)***

These results were accomplished with a similar strategy to the vote count/percentage by county.

An empty candidate options list and a candidate votes dictionary were defined.

![candidate_results](https://user-images.githubusercontent.com/107309793/177915472-876d364d-b8ad-496f-ac01-4a5fef54b8ea.png)

A conditional statement was utilized within the `For row in reader:` for loop which appends the unique candidate names from the election_results.csv file to a list and generates a vote count. The vote count is initiated to zero and incremented by 1.

![candidate_results_2](https://user-images.githubusercontent.com/107309793/177891156-0c52a018-8f37-4a4d-9fcf-be2751f5cea5.png)

The `candidate_name` variable was defined first in this loop and contains the candidate names extracted from the election_results.csv file.

At this point the candidate options list is populated with the 3 candidates from the election_results.csv file and the candidate votes dictionary is populated with the total vote count for each candidate.

The candidate votes dictionary is accessed in another for loop which retrives the vote count and assigns it to a variable (`votes`), and uses this value and the `total_votes` variable to calculate the percentage of votes (`vote_percentage`).

![candidate_results_3](https://user-images.githubusercontent.com/107309793/177892637-f44908ca-9f32-4d78-8f0c-c6e539d9a622.png)

This is then printed to the terminal (and the election_analysis.txt text file).

![candidate_results_4](https://user-images.githubusercontent.com/107309793/177892757-9e04c2c5-b2e1-4b22-b4ce-bb531b0d7da9.png)

This is the print statement code:

![candidate_results_5](https://user-images.githubusercontent.com/107309793/177893568-c5a82f86-8387-433e-a513-d642aa8e7915.png)

#### Winning Candidate Vote Count and Percent of Total

The candidate that won the election was ***Diana Degette*** with a vote count of 272,892 and percentage of 73.8% of the total votes. This was accomplished by utilizing the `for candidate_name in candidate_votes:` for loop from before which references the `candidate_votes` dictionary containing the candidates and their associated vote counts.

2 empty variables were defined prior to using this loop which will later be populated with the winning candidate and it's number of votes.

![winning_candidate_results](https://user-images.githubusercontent.com/107309793/177895167-e12b6048-96af-453b-80ca-5dc68388e144.png)

A conditional statement within the for loop checks for when `votes > winning_count `. While iterating through the `candidate_votes` dictionary, the code finds each candidate vote (`votes`) and checks to see if it is larger than the `winning_count` variable (which starts at zero). Each time the for loop satisfies this condition, the `winning_candidate` string is updated with that candidate and the `winning_count` is updated to the dictionary value with the highest count

The 2nd half of this if statement `vote_percentage > winning_percentage` results in the `winning_percentage` equal to the highest vote percent when it iterates through the candidate votes dictionary.

![winning_candidate_results_2](https://user-images.githubusercontent.com/107309793/177895242-0624a3d3-a1c1-404e-81b2-4a2a4aa7495b.png)

A winning candidate summary is printed into the election_analysis.txt file. With the following code:

![winning_candidate_results_3](https://user-images.githubusercontent.com/107309793/177895394-99b4375b-09ed-4fac-a437-785ee4e7eb5f.png)

![winning_candidate_results_4](https://user-images.githubusercontent.com/107309793/177895482-62d02528-1de9-48fc-b661-4c04fa81d2ea.png)

### Election-Audit Summary
This script as it stands provides the information requested; specifications of the vote counts/percentages for the 3 candidates and 3 counties included on the election_results.csv file supplied. It also summarizes the county with the largest turnout and the candidate that won the election (by popular vote). If additional data is added to the CSV file under the same format (Ballot ID, County, Candidate), the results of this election can be reevaluated to include any additional candidate and/or counties.

#### Modifications
The provided election_results.csv file is currently limited to the 3 fields mentioned above. In another election, additional fields might have more significance. An example could be vote method. Did the voters submit their ballot by mail? In person? The same for loops described above could be applied to new fields to determine a count of vote method which could be determined by county (or candidate). Other fields such as political affiliation might also provide insight on the voter population.

As long as the data provided in a future election includes U.S. states, this script could potentially be modified to include vote counts by state rather than county. It could have use in larger scale elections in this case. This would require a significantly larger election_results.csv file which could affect how well the code runs, but at a fundamental level (i.e. counting variables, performing calculations on vote count, etc.) should still work.


