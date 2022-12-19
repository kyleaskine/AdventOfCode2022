import re
import copy

#This is just part 1 for now

def processInput(line):
	input = line.split(',')
	updateGrid(int(input[0]),int(input[1]),int(input[2]))

def updateGrid(x, y, z):
	lavaGrid[x][y][z] = 1
	lavaCubes.append([x,y,z])
	
def checkSurfaceAreas():
	sumSA = 0
	for coords in lavaCubes:
		touchingCubes = 0
		x = coords[0]
		y = coords[1]
		z = coords[2]
		if lavaGrid[x+1][y][z] == 1:
			touchingCubes += 1
		if lavaGrid[x][y+1][z] == 1:
			touchingCubes += 1
		if lavaGrid[x][y][z+1] == 1:
			touchingCubes += 1
		if lavaGrid[x-1][y][z] == 1:
			touchingCubes += 1
		if lavaGrid[x][y-1][z] == 1:
			touchingCubes += 1
		if lavaGrid[x][y][z-1] == 1:
			touchingCubes += 1
		sumSA += (6 - touchingCubes)
	return sumSA

def createGrid(minLoc, maxLoc):
	i = minLoc
	while i < maxLoc:
		j = minLoc
		lavaGrid.append([])
		while j < maxLoc:
			k = minLoc
			lavaGrid[i].append([])
			while k < maxLoc:
				lavaGrid[i][j].append(0)
				k += 1
			j += 1
		i += 1
	
with open('day18.txt') as f:
	lavaGrid = []
	lavaCubes = []
	createGrid(0,25)
	while True:
		line = f.readline()
		if not line or line == '\n':
			break
		processInput(line)
	print("Part 1: " + str(checkSurfaceAreas()))