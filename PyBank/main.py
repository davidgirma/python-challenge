# Dependecies
import os
import csv
import pathlib

# Set the path for the CSV file
# https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
current_path = pathlib.Path(__file__).parent.resolve()
csvpath = os.path.join(current_path, 'Resources', 'budget_data.csv')
analysispath = os.path.join(current_path, 'Analysis')

# Open the CSV file
with open(csvpath) as csvfile:
    csvfile_read = csv.reader(csvfile, delimiter=',')
    header = next(csvfile_read)

    # Decalre all the variables/counters
    months = 0
    total_amount = 0
    change = 0
    total_change = 0
    previous_row = 0
    max_increase = 0
    month_max_increase = ""
    month_max_decrease = ""
    max_decrease = 0
    
    # Looping through the CSV file
    for row in csvfile_read:
            months += 1
            total_amount += int(row[1])
            
            # In order to start comparing from the second row of data
            if months > 1:
                change = int(row[1]) - previous_row
                previous_row = int(row[1])
                total_change += change

            
                # Validate if it's the biggest increase/decrease
                if change > 0:
                    if change > max_increase:
                        max_increase = change
                        month_max_increase = row[0]
                elif change < 0:
                    if change < max_decrease:
                        max_decrease = change
                        month_max_decrease = row[0]
            
            previous_row = int(row[1])

# Print the Financial Analysis
print("\nFinancial Analysis\n----------------------------")
print("Total Months: ", months)
print("Total: $", total_amount)
print("Average Change: $", round(total_change/(months-1), 2))
print("Greatest Increase in Profits:", month_max_increase, "($", max_increase, ")")
print("Greatest Decrease in Profits:", month_max_decrease, "($", max_decrease, ")\n")

# Create a txt file with the analysis
pathlib.Path(os.path.join(analysispath, "results.txt")).touch()
with open(os.path.join(analysispath, "results.txt"), "w") as f:
    f.write("Financial Analysis\n----------------------------")
    f.write("\nTotal Months: " + str(months))
    f.write("\nTotal: $" + str(total_amount))
    f.write("\nAverage Change: $"+ str(round(total_change/(months-1), 2)))
    f.write("\nGreatest Increase in Profits: "+ month_max_increase + " ($" + str(max_increase) + ")")
    f.write("\nGreatest Decrease in Profits: "+ month_max_decrease + " ($" + str(max_decrease) + ")")
