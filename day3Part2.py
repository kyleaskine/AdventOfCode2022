with open('day3.txt') as f:
	sum = 0;
	while True:
		line1 = f.readline()
		if not line1:
			print(sum)
			break
		line2 = f.readline()
		line3 = f.readline()
		array = list(line1)
		array2 = list(line2)
		array3 = list(line3)
		for c in array:
			if c in array2 and c in array3:
				intVal = ord(c)
				print(c)
				if intVal < 96:
					sum += intVal - 38
				else:
					sum += intVal - 96
				break