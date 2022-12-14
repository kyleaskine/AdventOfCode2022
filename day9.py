def updateTailLocation(headLoc, tailLoc):
	if abs(tailLoc[0] - headLoc[0]) == 2 and abs(tailLoc[1] - headLoc[1]) == 2:
		return [(headLoc[0] + tailLoc[0]) // 2, (headLoc[1]+ tailLoc[1]) // 2]
	if tailLoc[0] == headLoc[0] - 2:
		return [headLoc[0] - 1, headLoc[1]]
	if tailLoc[0] == headLoc[0] + 2:
		return [headLoc[0] + 1, headLoc[1]]
	if tailLoc[1] == headLoc[1] - 2:
		return [headLoc[0], headLoc[1] - 1]
	if tailLoc[1] == headLoc[1] + 2:
		return [headLoc[0], headLoc[1] + 1]
	return tailLoc
	
def updateHeadLocation(move, headLoc):
	if move == 'U':
		return [headLoc[0] + 1, headLoc[1]]
	if move == 'D':
		return [headLoc[0] - 1, headLoc[1]]
	if move == 'L':
		return [headLoc[0], headLoc[1] - 1]
	if move == 'R':
		return [headLoc[0], headLoc[1] + 1]
	raise Exception('Check input ' + move)
	
def parseMove(line):
	move = []
	input = line.split(' ')
	move.append(input[0])
	move.append(int(input[1]))
	return move
	
def checkDistinctTailLocs(tailLoc, masterTailLocs):
	if not tailLoc in masterTailLocs:
		return True
	return False

with open('day9.txt') as f:
	headLoc = [0,0]
	tailLoc = {}
	masterTailLocs = {}
	moves = 1
	while True:
		line = f.readline()
		if not line:
			print(len(masterTailLocs[1]))
			print(len(masterTailLocs[9]))
			break
		move = parseMove(line)
		while move[1] > 0:
			moves += 1
			print('MOVE ' + str(moves) + ': ' + move[0])
			headLoc = updateHeadLocation(move[0], headLoc)
			print(headLoc)
			tailLoc[0] = headLoc
			tailNum = 1
			while tailNum < 10:
				if not tailNum in tailLoc:
					tailLoc[tailNum] = [0,0]
					masterTailLocs[tailNum] = []
				tailLoc[tailNum] = updateTailLocation(tailLoc[tailNum - 1], tailLoc[tailNum])
				if checkDistinctTailLocs(tailLoc[tailNum], masterTailLocs[tailNum]):
					masterTailLocs[tailNum].append(tailLoc[tailNum])
				tailNum += 1
			print(tailLoc)
			move[1] -= 1