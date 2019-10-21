# python-challenge

PyBank Folder
  
  Contents:   In the PyBank folder you will find the program "main.py" and a copy of the result file "results.txt".
  
  Summary:  The "main.py" program loops through the "budget_data.csv" file, and does these things:
    - calculates a change value (starting at the 2nd month, current month P&L - previous month P&L)
    - creates a list of P&L change values (to be averaged later)
    - captures the greatest increase and decrease by basic conditional (i.e. "if change > int(row[1])"
    - counts the number of months through a basic iterator (i.e. "nuberOfMonths += 1 ")
    - summarizes all of the profit/loss values (i.e. "totalProfitLoss += int(row[1])")
    - using defined function "average", gets the average of the values in the change list
    - prints out results to screen
    - writes out results to file

PyPoll
  
  Contents: In the PyPoll folder you will find the program "main.py" and a copy of the result file "results.txt"
  
  Summary: The "main.py" program loops through the election file "election_data.csv" and does these things:
    - creates a list of dictionaries (keys: "name", "votes") called candidates
      - this is accomplished by looping through the candidates list for each row
        - if the row's candidate does not exist in the current dictionary "candidate", then append a new dictionary with votes of 0
      - if the row's candidate matches the dictionary candidate's name, then increment their vote counter (i.e. "candidate["votes"] += 1")
      - totalVotes is incremented by 1
    - once file is processed, the first part of the results are printed to screen (totalVotes)
    - the program then loops through the list of dictionaries "candidates"
      - their % of the total vote is calculated
      - the winning candidate is found out via a simple conditional
      - 1 row per candidate is printed out, showing: name, %vote (#votes)
    - The program finishes by writing out the results.txt file, repeating the process of printing (the exception being not figuring out the winner again)
