def isTreeVisibleNorth(matrix, i, j, height):
	if i < 0:
		return True
	elif matrix[i][j] >= height:
		return False
	return isTreeVisibleNorth(matrix, i - 1, j, height)
		
def isTreeVisibleSouth(matrix, i, j, height):
	if i == len(matrix):
		return True
	elif matrix[i][j] >= height:
		return False
	return isTreeVisibleSouth(matrix, i + 1, j, height)
		
def isTreeVisibleEast(matrix, i, j, height):
	if j == len(matrix[i]):
		return True
	elif matrix[i][j] >= height:
		return False
	return isTreeVisibleEast(matrix, i, j + 1, height)
		
def isTreeVisibleWest(matrix, i, j, height):
	if j < 0:
		return True
	elif matrix[i][j] >= height:
		return False
	return isTreeVisibleWest(matrix, i, j - 1, height)
	
def getNumVisibleTreesNorth(matrix, i, j, height):
	if i < 0:
		return 0
	elif matrix[i][j] >= height:
		return 1
	return 1 + getNumVisibleTreesNorth(matrix, i - 1, j, height)
		
def getNumVisibleTreesSouth(matrix, i, j, height):
	if i == len(matrix):
		return 0
	elif matrix[i][j] >= height:
		return 1
	return 1 + getNumVisibleTreesSouth(matrix, i + 1, j, height)
		
def getNumVisibleTreesEast(matrix, i, j, height):
	if j == len(matrix[i]):
		return 0
	elif matrix[i][j] >= height:
		return 1
	return 1 + getNumVisibleTreesEast(matrix, i, j + 1, height)
		
def getNumVisibleTreesWest(matrix, i, j, height):
	if j < 0:
		return 0
	elif matrix[i][j] >= height:
		return 1
	return 1 + getNumVisibleTreesWest(matrix, i, j - 1, height)

def isTreeVisible(matrix, i, j):
	if isTreeVisibleNorth(matrix, i - 1, j, matrix[i][j]):
		return 1
	if isTreeVisibleSouth(matrix, i + 1, j, matrix[i][j]):
		return 1
	if isTreeVisibleEast(matrix, i, j + 1, matrix[i][j]):
		return 1
	if isTreeVisibleWest(matrix, i, j - 1, matrix[i][j]):
		return 1
	return 0
	
def getScenicScore(matrix, i, j):
	north = getNumVisibleTreesNorth(matrix, i - 1, j, matrix[i][j])
	south = getNumVisibleTreesSouth(matrix, i + 1, j, matrix[i][j])
	east = getNumVisibleTreesEast(matrix, i, j + 1, matrix[i][j])
	west = getNumVisibleTreesWest(matrix, i, j - 1, matrix[i][j])
	return north * south * east * west

def findNumVisibleTrees(matrix):
	sum = 0
	i = 0
	while i < len(matrix):
		j = 0
		arr = matrix[i]
		while j < len(arr):
			sum += isTreeVisible(matrix,i,j)
			j += 1
		i += 1
	return sum
	
def findMaxScenicScore(matrix):
	maxScore = 0
	i = 0
	while i < len(matrix):
		j = 0
		arr = matrix[i]
		while j < len(arr):
			score = getScenicScore(matrix,i,j)
			if score > maxScore:
				maxScore = score
			j += 1
		i += 1
	return maxScore

with open('day8.txt') as f:
	matrix = []
	while True:
		line = f.readline()
		if not line:
			break
		arr = []
		for c in line:
			if c != '\n':
				arr.append(int(c))
		matrix.append(arr)
	print(findNumVisibleTrees(matrix))
	print(findMaxScenicScore(matrix))
		