import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#function to calculate average of a list of numbers
def average(numbers):
    
    #get count of numbers (denominator)
    length = len(numbers)
    
    #initialize total
    total = 0

    #loop through numbers, adding to get total
    for number in numbers:
        total = total + int(number)

    #return teh average, rounded to two decimal places
    return round(total / length, 2)

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    #setup the reader 
    csvreader = csv.reader(csvfile)
    
    #grab the header, skip to next row
    header = next(csvreader)

    #setup list to record the month to month change
    changes=[]

    #variable for the total
    totalProfitLoss = 0

    #variables to help the iteration and store the cumulative #'s
    previousMonth = ""
    previousPL = 0
    greatestIncreaseValue = 0
    greatestIncreaseMonth = ""
    greatestDecreaseValue = 0
    greatestDecreaseMonth = ""

    #number of months
    numberOfMonths = 0

    #looping through reader
    for row in csvreader:
        
        #if the previous month is not empty (which indicates 1st month), calculate the change
        if previousMonth != "":
            
            #calculate the difference between the current and previous month
            change = int(row[1]) - previousPL

            #append the change to the list so we can average it later
            changes.append(change)
            
            #see if the change is the largets increase or decrease, then record the values
            if change > greatestIncreaseValue:
                greatestIncreaseValue = change
                greatestIncreaseMonth = row[0]
            elif change < greatestDecreaseValue:
                greatestDecreaseValue = change
                greatestDecreaseMonth = row[0]

        #set the variables for the next iteration
        previousMonth = row[0]
        previousPL = int(row[1])

        #calculate the total
        totalProfitLoss += int(row[1])

        #increment # of months
        numberOfMonths += 1

    #calculate the average change
    averageChange = average(changes)    
    
    #return the values to the screen
    print("Financial Analysis")
    print("-------------------------------")
    print(f'Total Months: {numberOfMonths}')
    print(f'Total: ${totalProfitLoss}')
    print(f'Average Change: ${averageChange}')
    print(f'Greatest Increasse in Profits: {greatestIncreaseMonth} (${greatestIncreaseValue})')
    print(f'Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecreaseValue})')



