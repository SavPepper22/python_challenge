#First I need to import the csv library and module I will use.

import os
import csv

#Need to make an object using the name of the class I want to use the variables and values.
budget_data = os.path.join("budget_data.csv")
#Make empty lists so the csv values can be added.
profit = []
date = []
change_profit = []
value = 0
total_profit = 0
value = 0
#Open and read the CSV file.
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Extract field names and make a header.
    csv_header = next(csvreader)
    # Go through each row of data
    for row in csvreader :
        
        #Review and categorize the values and then add them to the empty lists.
        date.append(row[0])
        profit.append(int(row[1]))


for x in range(len(profit)):
    
    total_profit += (profit[x])


for i in range(len(profit)-1):
    change_profit.append(profit[i+1]-profit[i])


#Calculate the greatest increase/decrease in profits.
increase = max(change_profit)
decrease = min(change_profit)
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

#Calculate the average change.
avg_change = sum(change_profit)/len(change_profit)

#Displaying information
print("Financial Analysis")
print("-------------------------")

print(f"Total Months : {str(len(date))}")
print(f'Total: ${str(total_profit)}')
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits:{date[month_increase]} (${str(increase)})")
print(f"Greatest Increease in Profits:{date[month_decrease]} (${str(decrease)})")

# Ok now we are going to  make a text file.
with open("output.txt", 'w+') as f:

    f.write(f"Financial Analysis")
    f.write("\n")
    f.write("-------------------------")
    f.write("\n")
    f.write(f'Total Months : {str(len(date))}')
    f.write("\n")
    f.write(f"Total: ${str(total_profit)}")
    f.write("\n")
    f.write(f"Average Change: ${str(round(avg_change,2))}")
    f.write("\n")
    f.write(f"Greatest Increase in Profits:{date[month_increase]} (${str(increase)})")
    f.write("\n")
    f.write(f"Greatest Increease in Profits:{date[month_decrease]} (${str(decrease)})")











