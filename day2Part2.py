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
				thisScore = 3
			elif me == 'Y':
				thisScore = 4
			else:
				thisScore = 8
		elif oppo == 'B':
			if me == 'X':
				thisScore = 1
			elif me == 'Y':
				thisScore = 5
			else:
				thisScore = 9
		elif oppo == 'C':
			if me == 'X':
				thisScore = 2
			elif me == 'Y':
				thisScore = 6
			else:
				thisScore = 7
		total += thisScore
		print(oppo + ' ' + me + ' ' + str(thisScore))