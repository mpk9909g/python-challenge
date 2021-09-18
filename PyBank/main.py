import os
import csv



# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')



# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header_row = next(csvreader)

    #intialize variables for calcuations
    number_of_months = 0
    profit_loss = 0
    net_profit_loss = 0
    profit_loss_change = 0
    total_profit_loss_change = 0
    max_pl_increase = 0
    max_pl_decrease = 0

    #now do for loop to determine the results
    for row in csvreader:
        # first store the prior month (prior row) profit/loss
        prior_mo_profit_loss = profit_loss 
        month = row[0]

        #now store the contents of the current row
        profit_loss = int(row[1])
        number_of_months += 1

        # next do the calculations
        net_profit_loss+=profit_loss
        profit_loss_change = profit_loss - prior_mo_profit_loss
        total_profit_loss_change += profit_loss_change

        # do a conditional statement to identify the max increase in profit/loss
        if profit_loss_change > max_pl_increase:
            max_pl_increase = profit_loss_change
            month_max_pl_increase = month

        # do a conditional statement to identify the max decrease in profit/loss
        if profit_loss_change < max_pl_decrease:
            max_pl_decrease = profit_loss_change
            month_max_pl_decrease = month
        
        # do a conditional statement to identify the initial profit/loss entry, 
        # so as not to include it in the average change calculation
        if profit_loss == profit_loss_change:
            change_total = 0
        else:
            change_total+=profit_loss_change

    # calculate the average of the monthly profit/loss changes
    average_change=round(change_total/(number_of_months-1),2)

# now output results to terminal
print("\n")
print("- - - - - - - - - - - - - - - -")
print("Financial Analysis")
print("- - - - - - - - - - - - - - - -")
print(f"Total Months: {number_of_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {month_max_pl_increase} (${max_pl_increase})")
print(f"Greatest Decrease in Profits: {month_max_pl_decrease} (${max_pl_decrease})")
print("- - - - - - - - - - - - - - - -")




# now output result to text file.  This is pretty redundant but more or less
# the same code as above, inside a with open

pybank_text_output = 'analysis/pybank_text_output.txt'

with open (pybank_text_output,'w') as text:

    text.write("- - - - - - - - - - - - - - - -\n")
    text.write("Financial Analysis\n")
    text.write("- - - - - - - - - - - - - - - -\n")
    text.write(f"Total Months: {number_of_months}\n")
    text.write(f"Total: ${net_profit_loss}\n")
    text.write(f"Average Change: ${average_change}\n")
    text.write(f"Greatest Increase in Profits: {month_max_pl_increase} (${max_pl_increase})\n")
    text.write(f"Greatest Decrease in Profits: {month_max_pl_decrease} (${max_pl_decrease})\n")
    text.write("- - - - - - - - - - - - - - - -")
