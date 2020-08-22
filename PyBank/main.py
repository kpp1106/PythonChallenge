import csv
import os

file_path = "Resources/budget_data.csv"

TotalMonths = 0
TotalBudget = []
GreatestIncrease = []
GreatestDecrease = []

NetTotal = 0
Delta = []
PrevTotal = 0

current_value = 0
next_value = 0
change = 0
TotalChange = 0
AverageChange = 0
LargestChange = 0
SmallestChange = 0
LargeMonth = " "
SmallMonth = " "

with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        TotalMonths = TotalMonths + 1 #counting each row since the months are unique
        TotalBudget.append(int(row[1]))
        GreatestIncrease.append(str(row[0]))
        GreatestDecrease.append(str(row[0]))

counter = 0

for i in TotalBudget:
    NetTotal = NetTotal + i
    current_value = TotalBudget[counter]
    counter = counter + 1
    
    if (counter < TotalMonths):
        next_value = TotalBudget[counter]
        
    change = current_value - next_value
    
    if (SmallestChange > change):
        SmallestChange = change
        SmallMonth = GreatestIncrease[counter]

    if (LargestChange < change):
        LargestChange = change
        LargeMonth = GreatestDecrease[counter]

    TotalChange = TotalChange + change
    Delta.append(str(change))

AverageChange = TotalChange/(TotalMonths-1)

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${NetTotal}")
print(f"Average Change: ${AverageChange}")
print(f"Greatest Increase in Profits: {LargeMonth} (${LargestChange})")
print(f"Greatest Decrease in Profits: {SmallMonth} (${SmallestChange})")

output_file = os.path.join("Analysis","PyBankOut.csv")

with open(output_file, 'w') as csv_file:
    csv_file.write("Financial Analysis\n")
    csv_file.write("------------------\n")
    csv_file.write("Total Months: ")
    csv_file.write(str(TotalMonths))
    csv_file.write("\n")
    csv_file.write("Total: $")
    csv_file.write(str(NetTotal))
    csv_file.write("\n")
    csv_file.write("Average Change: $ ")
    csv_file.write(str(AverageChange))
    csv_file.write("\n")
    csv_file.write("Greatest Increase in Profits: ") 
    csv_file.write(LargeMonth)
    csv_file.write("($")
    csv_file.write(str(LargestChange))
    csv_file.write(")")
    csv_file.write("\n")
    csv_file.write("Greatest Decrease in Profits: ")
    csv_file.write(SmallMonth)
    csv_file.write("($")
    csv_file.write(str(SmallestChange))
    csv_file.write(")")


            

    
    