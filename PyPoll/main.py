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

uniquecandidate = []
for x in candidate:
    if x not in uniquecandidate:
        uniquecandidate.append(x)

print(uniquecandidate)

KhanTotal = 0
CorreyTotal = 0
LiTotal = 0
OTooleyTotal = 0

for i in candidate:
    if i == "Khan":
        KhanTotal = KhanTotal +1
    elif i == "Correy":
        CorreyTotal = CorreyTotal + 1
    elif i == "Li":
        LiTotal = LiTotal + 1
    elif i == "O'Tooley":
        OTooleyTotal = OTooleyTotal + 1
print(KhanTotal, CorreyTotal, LiTotal, OTooleyTotal)

KhanPercent = (KhanTotal/totalvotes)*100
CorreyPercent = (CorreyTotal/totalvotes)*100
LiPercent = (LiTotal/totalvotes)*100
OTooleyPercent = (OTooleyTotal/totalvotes)*100

print("Total Votes: "+ str(totalvotes))
print("Khan: " +str(KhanPercent)+ "(" +str(KhanTotal) +")")
print("Correy: "+ str(CorreyPercent)+ "(" +str(CorreyTotal) +")")
print("Li: " + str(LiPercent)+ "(" +str(LiTotal) +")")
print("O'Tooley: " + str(OTooleyPercent) + "(" +str(OTooleyTotal) +")")
print("Winner: Khan")