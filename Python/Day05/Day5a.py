def GetSeatID(boardingPass):
    return GetRow(boardingPass[:7]) * 8 + GetCol(boardingPass[7:])

def GetRow(rowVals):
    return int(rowVals.translate({ord(x): y for (x, y) in zip("BF","10")}), 2)

def GetCol(colVals):
    return int(colVals.translate({ord(x): y for (x, y) in zip("RL","10")}), 2)
    



content = open('input.txt', 'r').read().splitlines()
seatIDs = []
for boardingPass in content:
   seatIDs.append(GetSeatID(boardingPass))
print(max(seatIDs))
input("finished")