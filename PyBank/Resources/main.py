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
totalmonths

moneyList

for i in range(0, len(moneyList)):
    moneyList[i] = int(moneyList[i])

nettotal = sum(moneyList)
nettotal

changeList = []
for i in range (0, len(moneyList)-1):
    change = moneyList[i+1] - moneyList[i]
    changeList.append(change)
print(changeList)

len(changeList)

changeListAv = round(sum(changeList)/len(changeList),2)
changeListAv

for i in range(len(changeList)):
    if (changeList[i] == max(changeList)):
        maxchangedate = (dateList[i+1],max(changeList))
greatestincrease = str("Greatest Increase in Profits: " + str(maxchangedate))

for i in range(len(changeList)):
    if (changeList[i] == min(changeList)):
        minchangedate = (dateList[i+1],min(changeList))
greatestdecrease = str("Greatest Decrease in Profits: " + str(minchangedate))

print(f"Financial Analysis\n"
     "______________________________ \n")
print("Total Months: " + str(totalmonths))
print("Total Net Profits & Losses: " + "$"+ str(nettotal)+".00")
print("Average Change: " + "$"+ str(changeListAv))
print(greatestincrease)
print(greatestdecrease)

with open("budget_data.txt","w", newline="") as txtfile:
    print(f"Financial Analysis\n"
     "______________________________ \n",file = txtfile)
    print("Total Months: " + str(totalmonths),file = txtfile)
    print("Total Net Profits & Losses: " + "$"+ str(nettotal) +".00",file = txtfile)
    print("Average Change: " + "$"+ str(changeListAv),file = txtfile)
    print(greatestincrease,file = txtfile)
    print(greatestdecrease,file = txtfile)

