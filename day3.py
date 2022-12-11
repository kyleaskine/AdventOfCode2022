with open('day3.txt') as f:
	sum = 0;
	while True:
		line = f.readline()
		if not line:
			print(sum)
			break
		array = list(line)
		firstHalf = array[0:len(array) // 2]
		secondHalf = array[len(array) // 2: len(array)]
		for c in firstHalf:
			if c in secondHalf:
				intVal = ord(c)
				if intVal < 96:
					sum += intVal - 38
				else:
					sum += intVal - 96
				break