import copy

def processLine(line, cave):
	points = line.split(" -> ")
	coords = []
	for point in points:
		coord = point.split(",")
		coords.append([int(coord[0]), int(coord[1])])
	drawLines(coords, cave)
	
def drawLines(coords, cave):
	i = 1
	while i < len(coords):
		if coords[i][0] == coords[i-1][0]:
			drawVertLine(coords[i][1], coords[i-1][1], coords[i][0], cave)
		else:
			drawHorizLine(coords[i][0], coords[i-1][0], coords[i][1], cave)
		i += 1

def drawVertLine(start, end, x, cave):
	i = 0
	if start > end:
		temp = start;
		start = end;
		end = temp;
	while i <= end - start:
		if start + i not in cave:
			cave[start + i] = {}
		cave[start + i].update({x: 1})
		i += 1
		
def drawHorizLine(start, end, y, cave):
	i = 0
	if start > end:
		temp = start;
		start = end;
		end = temp;
	while i <= end - start:
		if y not in cave:
			cave[y] = {}
		cave[y].update({start + i: 1})
		i += 1
		
def processSand(cave):
	defXCoord = 500
	defYCoord = 0
	i = 0
	maxY = max(cave)
	while True:
		x = defXCoord
		y = defYCoord
		while True:
			if y > maxY:
				return i
			elif y + 1 not in cave:
				y += 1
			elif x not in cave[y + 1]:
				y += 1
			elif x - 1 not in cave[y + 1]:
				x -= 1
				y += 1
			elif x + 1 not in cave[y + 1]:
				x += 1
				y += 1
			else:
				if y not in cave:
					cave[y] = {}
				cave[y].update({x: 1})
				if x == 500 and y == 0:
					return i + 1
				break
		i += 1

with open('day14.txt') as f:
	cave = {}
	while True:
		line = f.readline()
		if not line:
			break
		processLine(line, cave)
	origCave = copy.deepcopy(cave)
	print("Part 1: " + str(processSand(cave)))
	cave = origCave
	floor = max(cave) + 2
	drawHorizLine(0,1000,floor, cave)
	print("Part 2: " + str(processSand(cave)))
	