with open('day2.txt') as f:
	total = 0;
	while True:
		line = f.readline()
		if not line:
			print('Total Score: ' + str(total))
			break
		rps = line.split(' ');
		oppo = rps[0];
		me = rps[1].strip();
		thisScore = 0;
		if oppo == 'A':
			if me == 'X':
				thisScore = 4
			elif me == 'Y':
				thisScore = 8
			else:
				thisScore = 3
		elif oppo == 'B':
			if me == 'X':
				thisScore = 1
			elif me == 'Y':
				thisScore = 5
			else:
				thisScore = 9
		elif oppo == 'C':
			if me == 'X':
				thisScore = 7
			elif me == 'Y':
				thisScore = 2
			else:
				thisScore = 6
		total += thisScore
		print(oppo + ' ' + me + ' ' + str(thisScore))