import os
import csv

csvpath = '/Users/elliottlevy/ucb-bel-data-pt-10-2020-u-c/01-Lesson-Plans/03-Python/Homework/PyBank/Resources/budget_data.csv'


with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)

    profit = 0
    total = 0
    total_months = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = " "
    greatest_decrease_month = " "

    for row in csvreader:
        profit = int(row[1])

        if profit > greatest_increase:
            greatest_increase = profit
            greatest_increase_month = row[0]

        if profit < greatest_decrease:
            greatest_decrease = profit
            greatest_decrease_month = row[0]
        
        total += profit
        total_months += 1
        profit = 0
    
    average_profit = total/total_months

    print("Financial Analysis")
    print("-------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average_profit}")
    print(f"Greatest Increase In Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease In Profits: {greatest_decrease_month} (${greatest_decrease})")

write_file = f"pybank_results_summary.txt"

filewriter = open(write_file, mode = 'w')

filewriter.write("Financial Analysis\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Months: {total_months}\n")
filewriter.write(f"Average Change: ${average_profit}\n")
filewriter.write(f"Greatest Increase In Profits: {greatest_increase_month} (${greatest_increase})\n")
filewriter.write("Greatest Decrease In Profits: {greatest_decrease_month} (${greatest_decrease})\n")

filewriter.close()


