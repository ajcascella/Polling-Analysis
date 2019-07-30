import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler)
    header = next(reader)
    dateList = []
    moneyList = []
    for row in reader:
        dateList.append(row[0])
        moneyList.append(row[1])

totalmonths = (len(dateList))
print(totalmonths)

for i in range(0, len(moneyList)):
    moneyList[i] = int(moneyList[i])

nettotal = sum(moneyList)
print(nettotal)

changeList = []
changeList.append(0)
for i in range (0,len(moneyList)-1):
    change = moneyList[i+1] - (moneyList[i])
    changeList.append(change)
print(changeList)

changeListAv = round(sum(changeList)/len(changeList),2)
print(changeListAv)

for i in range(0,len(changeList)):
    if (changeList[i] == max(changeList)):
        maxchangedate = (dateList[i],max(changeList))
greatestincrease = str(print("Greatest Increase in Profits: " + str(maxchangedate)))

for i in range(0,len(changeList)):
    if (changeList[i] == min(changeList)):
        minchangedate = (dateList[i],min(changeList))
greatestdecrease = str(print("Greatest Decrease in Profits: " + str(minchangedate)))

print(f"Financial Analysis\n"
     "______________________________ \n")
print("Total Months: " + str(totalmonths))
print("Total Net Profits & Losses: " + "$"+ str(nettotal))
print("Average Change: " + "$"+ str(changeListAv))