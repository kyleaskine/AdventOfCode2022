import re

def processInput(line):
	input = line.split(": ")
	right = input[1]
	digit = re.match("^(\d+)$", right)
	equation = re.match("^([a-z]{4}) (.?) ([a-z]{4})$", right)
	if digit:
		right = int(digit.group(1))
	else:
		right = [equation.group(1), equation.group(2), equation.group(3)]
	equations[input[0]] = right

def calcAnswer(key):
	if type(equations[key]) is int:
		return equations[key]
	
	equ = equations[key]
	if equ[1] == '+':
		return calcAnswer(equ[0]) + calcAnswer(equ[2])
	if equ[1] == '-':
		return calcAnswer(equ[0]) - calcAnswer(equ[2])
	if equ[1] == '*':
		return calcAnswer(equ[0]) * calcAnswer(equ[2])
	if equ[1] == '/':
		return int(calcAnswer(equ[0]) / calcAnswer(equ[2]))

def findHumn(key):
	if key == 'humn':
		pathToHumn.insert(0, key)
		return True
	if type(equations[key]) is int:
		return False
	
	equ = equations[key]
	if findHumn(equ[0]) or findHumn(equ[2]):
		pathToHumn.insert(0, key)
		return True
	return False
	
def calcPartTwo(key, goal, oldNumber):
	if key == goal:
		return oldNumber
	
	nextStep = pathToHumn.pop(0)
	
	equ = equations[key]
	otherSide = 0
	if equ[0] != nextStep:
		otherSide = calcAnswer(equ[0])
	else:
		otherSide = calcAnswer(equ[2])
	
	if oldNumber is not None:
		if equ[1] == '+':
			oldNumber = oldNumber - otherSide
		if equ[1] == '-':
			if equ[0] != nextStep:
				oldNumber = otherSide - oldNumber
			else:
				oldNumber = oldNumber + otherSide
		if equ[1] == '*':
			oldNumber = int(oldNumber / otherSide)
		if equ[1] == '/':
			if equ[0] != nextStep:
				oldNumber = int(otherSide / oldNumber)
			else:
				oldNumber = oldNumber * otherSide
	else:
		oldNumber = otherSide
	
	return calcPartTwo(nextStep, goal, oldNumber)
	

with open('day21.txt') as f:
	equations = {}
	while True:
		line = f.readline()
		if not line or line == '\n':
			break
		processInput(line)
	
	print("Part 1: " + str(calcAnswer("root")))
	pathToHumn = []
	findHumn("root")
	equations["root"][1] = "="
	print("Part 2: " + str(calcPartTwo(pathToHumn.pop(0), "humn", None)))