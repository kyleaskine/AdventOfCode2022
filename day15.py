import re
import math

def processLine(line, cave):
	splitLine = line.split(':')
	sensor = splitLine[0]
	beacon = splitLine[1]
	sensor = processSensor(sensor, cave)
	beacon = processBeacon(beacon, cave)
	i = findManhattanDist(sensor, beacon)
	cave.append([sensor[0], sensor[1], beacon[0], beacon[1], i])

def processSensor(sensor, cave):
	m = re.match('^Sensor at x=(-?\d+), y=(-?\d+)', sensor)
	x = int(m.group(1))
	y = int(m.group(2))
	return [x,y]
	
def processBeacon(beacon, cave):
	m = re.match('^ closest beacon is at x=(-?\d+), y=(-?\d+)', beacon)
	x = int(m.group(1))
	y = int(m.group(2))
	return [x,y]

def findManhattanDist(sensor, beacon):
	x = sensor[0]
	y = sensor[1]
	i = 0
	while beacon[0] > x:
		i += 1
		x += 1
	while beacon[0] < x:
		i += 1
		x -= 1
	while beacon[1] > y:
		i += 1
		y += 1
	while beacon[1] < y:
		i += 1
		y -= 1
	return i

def findNoBeaconLocations(sbd, caveLine):
	sum = None
	sensorX = sbd[0]
	sensorY = sbd[1]
	beaconX = sbd[2]
	beaconY = sbd[3]
	i = sbd[4]
	rowsAway = abs(caveLine - sensorY)
	if rowsAway <= i:
		sum = [sensorX - (i - rowsAway), sensorX + (i - rowsAway)]
		if beaconY == caveLine:
			if beaconX == sum[0]:
				sum[0] += 1
			else:
				sum[1] -= 1
			if sum[0] > sum[1]:
				sum = None
	return sum

def noBeaconLocationsRangeRowY(cave, y):
	i = 0
	range = []
	for sbd in cave:
		locs = findNoBeaconLocations(sbd, y)
		if locs:
			range.append(locs)
	finalResult = []
	for loc in range:
		if finalResult == []:
			finalResult.append(loc)
		else:
			finalResult = processNewLocRange(loc, finalResult)
	finalResult = combineResults(finalResult)
	return [sumRanges(finalResult), finalResult]

def sumRanges(range):
	sum = 0
	for vector in range:
		sum += vector[1] - vector[0] + 1
	return sum
	
def processNewLocRange(loc, range):
	i = 0
	for vector in range:
		if loc[0] < vector[0]:
			if loc[1] < vector[0]:
				range = range[:i] +[loc] + range[i:]
				return range
			if loc[1] < vector[1]:
				range[i][0] = loc[0]
				return range
			else:
				range[i] = loc
				return range
		elif loc[0] <= vector[1]:
			if loc[1] > vector[1]:
				range[i][1] = loc[1]
				return range
			else:
				return range
		i += 1
	range.append(loc)
	return range

def combineResults(range):
	i = 1
	output = []
	while i < len(range):
		if range[i-1][1] + 1 >= range[i][0]:
			output.append([range[i-1][0], max(range[i][1], range[i-1][1])])
			return combineResults(output[:i] + range[i+1:])
		else:
			output.append(range[i-1])
		i += 1
	return range
	
def cullToSize(range, minX, maxX):
	output = []
	for vector in range:
		if vector[0] < minX and vector[1] > maxX:
			output.append([minX, maxX])
		elif vector[0] < minX:
			if vector[1] >= minX:
				output.append([minX,vector[1]])
		elif vector[1] > maxX:
			if vector[0] <= maxX:
				output.append([vector[0],maxX])
		else:
			output.append(vector)
	return output
	
def findBeacon(cave):
	row = 0
	while row <= 4000000:
		if distressBeaconOnRow(cave, row):
			return distressBeaconOnRow
		row += 1
	
def distressBeaconOnRow(cave, row):
	minX = 0
	maxX = 4000000
	ranges = noBeaconLocationsRangeRowY(cave, row)[1]
	ranges = cullToSize(ranges, minX, maxX)
	if len(ranges) > 1:
		print("Row " + str(row) + ": " + str(ranges) + " Frequency:" + str((ranges[0][1] + 1) * 4000000 + row))
		
	
with open('day15.txt') as f:
	cave = []
	while True:
		line = f.readline()
		if not line:
			break
		processLine(line, cave)
	print("Part 1: " + str(noBeaconLocationsRangeRowY(cave, 2000000)[0]))
	findBeacon(cave) #i admit it, this only gives me the 5 possibilities and i checked them manually