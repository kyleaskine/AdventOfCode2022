import re

def parseList(line, start):
	i = start
	retVal = []
	while True:
		c = line[i]
		if c=='[':
			output = parseList(line, i+1)
			retVal.append(output[0])
			i = output[1]
		elif c==',':
				i+=1
		elif c==']':
			i += 1
			break
		else:
			num = ''
			while re.search('\d', c):
				num += c
				i += 1
				c = line[i]
			retVal.append(int(num))
	return [retVal, i]

def compareList(left, right):
	currIndex = 0
	funcOutput = None
	while True:
		if currIndex == len(left) and len(left) < len(right):
			return True
		elif currIndex == len(right) and len(left) > len(right):
			return False
		elif currIndex == len(left):
			return None

		leftVal = left[currIndex]
		rightVal = right[currIndex]
		
		if type(leftVal) != type(rightVal):
			if type(leftVal) is int:
				leftVal = [leftVal]
			else:
				rightVal = [rightVal]
			funcOutput = compareList(leftVal, rightVal)
		elif type(leftVal) is list:
			funcOutput = compareList(leftVal, rightVal)
		else:
			if left < right:
				return True
			elif right < left:
				return False
		
		if funcOutput == True:
			return True
		elif funcOutput == False:
			return False
			
		currIndex += 1
		
	return None

def lessThan(listOne, listTwo):
	return compareList(listOne, listTwo)

with open('day13.txt') as f:
	pairNum = 1
	sum = 0
	two = [[2]];
	six = [[6]];
	numLTTwo = 1;
	numLTSix = 2;
	while True:
		line = f.readline()
		if not line:
			print("Part 1: " + str(sum))
			print("Part 2: " + str(numLTTwo) + " " + str(numLTSix))
			print("Part 2: " + str(numLTTwo * numLTSix))
			break
		left = parseList(line, 1)[0]
		line = f.readline()
		right = parseList(line, 1)[0]
		line = f.readline()
		
		if compareList(left, right):
			#print("Pair " + str(pairNum) + " matches!")
			sum += pairNum
		#else:
			#print("Pair " + str(pairNum) + " does not match")
		
		if lessThan(left, two):
			numLTTwo += 1
			numLTSix += 1
		elif lessThan(left, six):
			numLTSix += 1
		if lessThan(right, two):
			numLTTwo += 1
			numLTSix += 1
		elif lessThan(right, six):
			numLTSix += 1
		
		pairNum += 1