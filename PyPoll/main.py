import csv
import os

file_path = "Resources/election_data.csv"

TotalVotes = 0
CandidateList = []
uniqueCandidate_list = []
Votes_list = []
groupedVotes_list = []

with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        TotalVotes = TotalVotes + 1                                                                                                                                                                                                                                                                         
        CandidateList.append(row[2])
        Votes_list.append(row[0])
        
counter = 0
Winner = ""

CandidateList.sort()
for x in CandidateList:
    if x not in uniqueCandidate_list:
        uniqueCandidate_list.append(x)
        groupedVotes_list.append(counter)
        counter = 1
    else:
        counter = counter + 1

groupedVotes_list.append(counter)

LargestVotes = max(groupedVotes_list)

indexLarge = groupedVotes_list.index(max(groupedVotes_list))

percentVote_List = []
percentCalculation = 0

counter = 0

for x in groupedVotes_list:
    percentCalculation = 100*groupedVotes_list[counter]/TotalVotes
    percentVote_List.append(round(percentCalculation))
    counter = counter + 1

print("Election Results")
print("------------")
print(f"Total Votes: {TotalVotes}")
print("------------")

counter = 0
for x in uniqueCandidate_list:
        print(f"{x} : {percentVote_List[counter+1]}% ({groupedVotes_list[counter+1]})")
        counter = counter + 1
        
counter = 0
output_file = os.path.join("Analysis", "PyPollOut.csv")

with open(output_file, 'w') as csv_file:
    csv_file.write("Election Results\n")
    csv_file.write("-------------------------------\n")
    csv_file.write("Total Votes: ")
    csv_file.write(str(TotalVotes))
    csv_file.write("\n")
    csv_file.write("-------------------------------\n")
    for x in uniqueCandidate_list:
        csv_file.write(f"{x} : {percentVote_List[counter+1]}% ({groupedVotes_list[counter+1]})")
        csv_file.write("\n")
        counter = counter + 1
    
#     csv_file.write(str(TotalVotes))
#     csv_file.write("\n")
#     csv_file.write("Total: $")
#     csv_file.write(str(NetTotal))
#     csv_file.write("\n")
#     csv_file.write("Average Change: ")
#     csv_file.write(str(AverageChange))
#     csv_file.write("\n-----")
#     csv_file.write("Greatest Increase in Profits: ") 
#     csv_file.write(LargeMonth)
#     csv_file.write("($")
#     csv_file.write(str(LargestChange))
#     csv_file.write(")")
#     csv_file.write("\n-----")
#     csv_file.write("Greatest Decrease in Profits: ")
#     csv_file.write(SmallMonth)
#     csv_file.write("($")
#     csv_file.write(str(SmallestChange))
#     csv_file.write(")")


            

    
    