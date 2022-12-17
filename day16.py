import re
import copy

#This currently is far too slow to complete part II, will look at later (I hope)

def processLine(line, cave):
	m = re.match("^Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)$", line)
	room = m.group(1)
	flow = int(m.group(2))
	rawPaths = m.group(3)
	rawPaths = rawPaths.split(', ')
	paths = []
	for path in rawPaths:
		paths.append(path)
	cave[room] = [flow, paths]

def findValves(cave):
	valveRooms = {}
	for room in cave:
		if cave[room][0] > 0 or room == 'AA':
			valveRooms[room] = cave[room]
	for valve in valveRooms:
		valveDistances = []
		for distances in valveRooms[valve][2]:
			if distances[0] in valveRooms and distances[0] != 'AA':
				valveDistances.append(distances)
		valveRooms[valve][2] = valveDistances
	return valveRooms

def buildGraph(cave):
	i = 0
	for startRoom in cave:
		fastestPath = findFastestPaths(startRoom, cave)

def findFastestPaths(startRoom, cave):
	visited = [startRoom]
	toVisit = [[startRoom, 0]]
	distances = []
	while toVisit:
		room = toVisit.pop(0)
		depth = room[1]
		distances.append(room)
		for adjRoom in cave[room[0]][1]:
			if adjRoom not in visited:
				visited.append(adjRoom)
				toVisit.append([adjRoom, depth + 1])
	cave[startRoom].append(distances)
	
def findAllPaths(valves, startRoom, visited, timer, timerArray):
	if(startRoom != 'AA'):
		timer += 1
		visited.append(startRoom)
		timerArray.append(timer)		
	if len(visited) == len(valves) - 1:
		masterPaths.append([visited, timerArray])
		return
	for room in valves[startRoom][2]:
		if room[0] not in visited and timer + room[1] < 29:
			findAllPaths(valves, room[0], visited.copy(), timer + room[1], timerArray.copy())
		elif timer + room[1] >= 29:
			masterPaths.append([visited, timerArray])
			return

def nestedPaths(masterPaths):
	i = 0
	for path in masterPaths:
		j = i + 1
		while j < len(masterPaths):
			currArray = []
			currArray.append(path)
			currArray.append(masterPaths[j])
			multiPath.append(mergeArrays(currArray))
			j += 1
		i += 1
		if i % 100 == 0:
			print(i)
			input("Hit Key")

def mergeArrays(currPath):
	finalRoomArray = []
	finalTimeArray = []
	i = 0
	j = 0
	while True:
		if i == len(currPath[0][0]) and j == len(currPath[1][0]):
			break
		elif i == len(currPath[0][0]):
			finalRoomArray.append(currPath[1][0][j])
			finalTimeArray.append(currPath[1][1][j])
			j += 1
		elif j == len(currPath[1][0]):
			finalRoomArray.append(currPath[0][0][i])
			finalTimeArray.append(currPath[0][1][i])
			i += 1
		elif currPath[0][1][i] < currPath[1][1][j]:
			finalRoomArray.append(currPath[0][0][i])
			finalTimeArray.append(currPath[0][1][i])
			i += 1
		else:
			finalRoomArray.append(currPath[1][0][j])
			finalTimeArray.append(currPath[1][1][j])
			j += 1
	return [finalRoomArray, finalTimeArray]
		

def releaseMostPressure(valves, path):
	maxPressureReleased = 0
	for pathTimer in path:
		openedValves = []
		i = 0
		pressureReleased = 0
		for room in pathTimer[0]:
			if room not in openedValves:
				pressureReleased += max(0,(30 - pathTimer[1][i]) * valves[room][0])
				openedValves.append(room)
			i += 1
		if pressureReleased > maxPressureReleased:
			print("New Record: " + str(pathTimer[0]) + " - " + str(pressureReleased))
			maxPressureReleased = pressureReleased
	
with open('day16.txt') as f:
	cave = {}
	while True:
		line = f.readline()
		if not line or line == '\n':
			break
		processLine(line, cave)
	buildGraph(cave)
	valves = findValves(cave)
	masterPaths = []
	findAllPaths(valves, 'AA', [], 0, [])
	print(len(masterPaths))
	releaseMostPressure(valves, masterPaths)
	masterPaths = []
	multiPath = []
	findAllPaths(valves, 'AA', [], 4, [])
	nestedPaths(masterPaths)
	print(len(multiPath))
	releaseMostPressure(valves, multiPath)