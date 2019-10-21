<b># python-challenge</b><br/>
<i>By Michael Dowlin (10/21/19)</i><br/>

PyBank Folder<br/>
  
Contents<br/>
In the PyBank folder you will find the program "main.py" and a copy of the result file "results.txt".<br/>
<br/>  
Summary<br/>
The "main.py" program loops through the "budget_data.csv" file, and does these things:<br/>
•	calculates a change value (starting at the 2nd month, current month P&L - previous month P&L)<br/>
•	creates a list of P&L change values (to be averaged later)<br/>
•	captures the greatest increase and decrease by basic conditional (i.e. "if change > int(row[1])"<br/>
•	counts the number of months through a basic iterator (i.e. "nuberOfMonths += 1 ")<br/>
•	summarizes all of the profit/loss values (i.e. "totalProfitLoss += int(row[1])")<br/>
•	using defined function "average", gets the average of the values in the change list<br/>
•	prints out results to screen<br/>
•	writes out results to file<br/>
<br/>
PyPoll<br/>
<br/>  
Contents<br/>
In the PyPoll folder you will find the program "main.py" and a copy of the result file "results.txt"<br/>
<br/>
Summary<br/>
The "main.py" program loops through the election file "election_data.csv" and does these things:<br/>
•	creates a list of dictionaries (keys: "name", "votes") called candidates<br/>
•	this is accomplished by looping through the candidates list for each row<br/>
  o	if the row's candidate does not exist in the current dictionary "candidate", then append a new dictionary with votes of 0<br/>
•	if the row's candidate matches the dictionary candidate's name, then increment their vote counter (i.e. "candidate["votes"] += 1")<br/>
•	totalVotes is incremented by 1<br/>
•	once file is processed, the first part of the results are printed to screen (totalVotes)<br/>
•	the program then loops through the list of dictionaries "candidates"<br/>
  o	their % of the total vote is calculated<br/>
  o	the winning candidate is found out via a simple conditional<br/>
  o	1 row per candidate is printed out, showing: name, %vote (#votes)<br/>
•	The program finishes by writing out the results.txt file, repeating the process of printing (the exception being not figuring out the winner again)
