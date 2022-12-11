with open('day4.txt') as f:
	fullyOverlap = 0
	partiallyOverlap = 0
	while True:
		line = f.readline()
		if not line:
			print('Fully Overlapping: ' + str(fullyOverlap))
			print('Partially Overlapping: ' + str(partiallyOverlap))
			break
		assignments = line.split(',')
		first = assignments[0].split('-')
		second = assignments[1].split('-')
		startFirst = int(first[0])
		endFirst = int(first[1])
		startSecond = int(second[0])
		endSecond = int(second[1])
		if startFirst <= startSecond and endFirst >= endSecond :
			fullyOverlap += 1
		elif startSecond <= startFirst and endSecond >= endFirst :
			fullyOverlap += 1
		if startFirst <= startSecond and endFirst >= startSecond:
			print(line)
			partiallyOverlap += 1
		elif startFirst <= endSecond and endFirst >= endSecond:
			print(line)
			partiallyOverlap += 1
		elif startSecond <= startFirst and endSecond >= startFirst:
			print(line)
			partiallyOverlap += 1
		elif startSecond <= endFirst and endSecond >= endFirst:
			print(line)
			partiallyOverlap += 1