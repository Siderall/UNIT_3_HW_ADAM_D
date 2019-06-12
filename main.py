import os
import csv

data = os.path.join("Resources", "budget_data.csv")

months = []
budget = []

with open(data, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)

    for row in csvreader:
        months.append(row[0])
        budget.append(int(row[1]))

months_total = len(months)
budget_net_total = sum(budget)

budget_change = []
i = 0
j = 0
for i in range(0, months_total):
  if i == 0:
    budget_change.append(0)
  else: 
    budget_change.append(int(budget[i])-int(budget[j]))
    j += 1

total_budget_change = 0
k = 0
for k in range(len(months)):
    total_budget_change = total_budget_change + int(budget_change[k])

average_budget_change = int(total_budget_change)/int(months_total - 1)

max_budget_change = max(budget_change)
max_index = budget_change.index(max_budget_change)
max_month = months[max_index]

min_budget_change = min(budget_change)
min_index = budget_change.index(min_budget_change)
min_month = months[min_index]

print("Financial Analysis")
print("----------------------------")
print("Total Months: "+ str(months_total))
print("Total: $" + str(budget_net_total))
print("Average Change: $" + str(average_budget_change))
print("Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_budget_change) + ")")
print("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(min_budget_change) + ")")

write_file = f"pybank_financial_summary.txt"
filewriter = open(write_file, mode = 'w')

filewriter.write(f"Financial Analysis:\n")
filewriter.write("-------------------------------------------------------\n")
filewriter.write(f"Total Months: {months_total}\n")
filewriter.write(f"Total Revenue: ${budget_net_total}\n")
filewriter.write(f"Average Revenue Change: ${average_budget_change}\n")
filewriter.write(f"Greatest Increase in Revenue: {max_month} (${max_budget_change}) \n")
filewriter.write(f"Greatest Decrease in Revenue: {min_month} (${min_budget_change})\n")
filewriter.write("")

filewriter.close()

#God damn that was hard! ;)