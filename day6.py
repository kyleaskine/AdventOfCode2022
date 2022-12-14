def areAllDifferent(last4):
	return len(set(last4)) == len(last4)
	
def findFirstArrayAllDifferent(line, arrayLength):
	i = 0
	lastXChars = []
	while i < arrayLength:
		lastXChars.append(line[i])
		i += 1
	while i < len(line) and not areAllDifferent(lastXChars):
		lastXChars[i % arrayLength] = line[i]
		i += 1
	print('First Array length ' + str(arrayLength) + ' with all different characters: ' + str(i))

with open('day6.txt') as f:
	line = f.readline()
	findFirstArrayAllDifferent(line, 4)
	findFirstArrayAllDifferent(line, 14)