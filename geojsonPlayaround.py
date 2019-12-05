referendum = {
    "Leave": 17410742,
    "Remain": 16141241
}

leave = {
    "Conservatives": .58,
    "Labour": .13,
    "Lib Dems": .04,
    "Brexit": .20
}

remain = {
    "Conservatives": .18,
    "Labour": .42,
    "Lib Dems": .29,
    "Brexit": .01
}



for k, v in leave.items():
    leave[k] = round(v * referendum["Leave"])
print(leave)

for k, v in remain.items():
    remain[k] = round(v * referendum["Leave"])
print(remain)

parties =["Conservative", "Labour", "LibDems", "Brexit"]
remLst = []
for value in remain:
    remLst.append(remain[value])
print(remLst)


leaveLst = []
for value in leave:
    leaveLst.append(leave[value])
print(leaveLst)

total = [x + y for x,y in zip(remLst, leaveLst)]
print(total)


pop = sum(total)
print(pop)
electionPrediction = {key: value for key, value in zip(parties, total)}
print(electionPrediction)

for k, v in electionPrediction.items():
    electionPrediction[k] = round((electionPrediction[k]/pop)*590)

print(electionPrediction)




