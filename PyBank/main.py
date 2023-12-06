#PyBank python code
#Import functions that will be used
import os
import csv

#Collect data from csv in Resources folder & set output file
budgetdata = os.path.join('Resources', 'budget_data.csv')
budgetoutput = os.path.join('analysis', 'budget_output.txt')

#Set tracking/calc parameters, pl refers to profit/loss
currentpl = 0
prevpl = 0
netpl = 0
plchange = 0
plchangelist = []
months = []

with open(budgetdata, 'r') as csvfile:

    #Setup csvreader and skip the first row which contains headers
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #print(header) #test reader

    for row in csvreader:

        #Extract profit/loss for this month(row)
        currentpl = int(row[1])
        #Track net profit/loss as csv is read
        netpl = netpl + currentpl
        
        #Calculate change in profit/loss for this month(row)
        plchange = currentpl - prevpl

        #Add this month(row) pl change to the profit/loss change storage list
        #First entry will be a false piece of data
        plchangelist.append(plchange)

        #Add this rows month title to the month storage list
        months.append(row[0])
        
        #Reassign previous profit/loss for next loop cycle (to calc change)
        prevpl = currentpl

    #Discard first entry (false data) in plchangelist as changes start month 2 onwards
    plchangelist.pop(0)

    #Calculate sum of profit and losses
    plsum = sum(plchangelist)
    #Determine total number of months (rows)
    num_months = len(months)
    
    #print(months)
    #print(plchangelist)
    #print("sum: " + str(plsum) + ". number of months: " + str(num_months))

    #Calculate average profit/loss
    plaverage = round(plsum/(num_months-1), 2) #As there is 85 instances of monthly changes but 86 months in total

    #Determine highest and lowest profit/loss
    highestpl = max(plchangelist)
    lowestpl = min(plchangelist)

    #Determine month associated with highest and lowest profit/loss
    highestplmonth = months[plchangelist.index(highestpl)]
    lowestplmonth = months[plchangelist.index(lowestpl)]

#Print out all results to terminal
print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(num_months))
print("Total: $" + str(netpl))
print("Average Change: $" + str(plaverage))
print("Greatest Increase in Profits: " + highestplmonth + " $" + str(highestpl))
print("Greatest Decrease in Profits: " + lowestplmonth + " $" + str(lowestpl))

#Opening output file to write results to
with open(budgetoutput, 'w') as outputfile:

    #Write results to new file budget_output.txt
    outputfile.write("Financial Analysis\n")
    outputfile.write("--------------------------\n")
    outputfile.write("Total Months: " + str(num_months) + "\n")
    outputfile.write("Total: $" + str(netpl) + "\n")
    outputfile.write("Average Change: $" + str(plaverage) + "\n")
    outputfile.write("Greatest Increase in Profits: " + highestplmonth + " $" + str(highestpl) + "\n")
    outputfile.write("Greatest Decrease in Profits: " + lowestplmonth + " $" + str(lowestpl) + "\n")