import os
import csv

csvpath = os.path.join("election_data.csv")
with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler)
    header = next(reader)
    voterid = []
    county = []
    candidate = []
    for row in reader:
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

totalvotes = len(voterid)
print(totalvotes)

uniquecandidate = {}
for x in candidate:
    if x not in uniquecandidate:
        uniquecandidate[x] = 1
    else:
        uniquecandidate[x] = uniquecandidate[x] + 1

print(uniquecandidate)

for x in uniquecandidate:
    print('key: ' + x + ", value: " + str(uniquecandidate[x]))

uniquecandidate['Khan']

KhanPercent = round((uniquecandidate["Khan"]/totalvotes)*100,2)
CorreyPercent = round((uniquecandidate['Correy']/totalvotes)*100,2)
LiPercent = round((uniquecandidate['Li']/totalvotes)*100,2)
OTooleyPercent = round((uniquecandidate["O'Tooley"]/totalvotes)*100,2)

print("Total Votes: "+ str(totalvotes))
print("Khan: " +str(KhanPercent)+ "% " + "(" +str(uniquecandidate['Khan']) +")")
print("Correy: "+ str(CorreyPercent)+"% " + "(" +str(uniquecandidate['Correy']) +")")
print("Li: " + str(LiPercent)+ "% " +"(" +str(uniquecandidate['Li']) +")")
print("O'Tooley: " + str(OTooleyPercent) + "% " +"(" +str(uniquecandidate["O'Tooley"]) +")")
print("Winner: ")

with open("poll_data.txt","w", newline="") as txtfile:
    print("Total Votes: "+ str(totalvotes),file = txtfile)
    print("Khan: " +str(KhanPercent)+ "% " + "(" +str(uniquecandidate['Khan']) +")",file = txtfile)
    print("Correy: "+ str(CorreyPercent)+"% " + "(" +str(uniquecandidate['Correy']) +")",file = txtfile)
    print("Li: " + str(LiPercent)+ "% " +"(" +str(uniquecandidate['Li']) +")",file = txtfile)
    print("O'Tooley: " + str(OTooleyPercent) + "% " +"(" +str(uniquecandidate["O'Tooley"]) +")",file = txtfile)
    print("Winner: ",file = txtfile)

