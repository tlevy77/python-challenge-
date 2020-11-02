import os
import csv

csvpath = "/Users/elliottlevy/ucb-bel-data-pt-10-2020-u-c/01-Lesson-Plans/03-Python/Homework/PyPoll/Resources/election_data.csv"

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)

    total_votes = 0
    candidate_list = []
    candidate_votes = []
    candidate_percent = []
    winner = " "
    winner_index = 0

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_list:
            candidate_index = candidate_list.index(candidate)
            candidate_votes[candidate_index] = candidate_votes[candidate_index]+1
        else:
            candidate_list.append(candidate)
            candidate_votes.append(1)

    for count in range(len(candidate_list)):
        vote_percent = round(candidate_votes[count]/total_votes * 100, 3)
        candidate_percent.append(vote_percent)
    
    winner_index = candidate_percent.index(max(candidate_percent))
    winner = candidate_list[winner_index]

print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for count in range(len(candidate_list)):
    print(f"{candidate_list[count]}: {candidate_percent[count]}% ({candidate_votes[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

write_file = f"pypoll_results_summary.txt"

filewriter = open(write_file, mode = 'w')

filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {total_votes}\n")
for count in range(len(candidate_list)):
    filewriter.write(f"{candidate_list[count]}: {candidate_percent[count]}% ({candidate_votes[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

filewriter.close()

        
