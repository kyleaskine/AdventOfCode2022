with open('day1Input.txt') as f:
	maxCalories = [];
	currCalories = 0;
	while True:
		line = f.readline()
		if not line:
			maxCalories.sort(reverse=True)
			print('Max Calories: ' + str(maxCalories[0] ))
			print('Sum of Top Three Calories: ' + str(maxCalories[0] + maxCalories[1] + maxCalories[2]))
			print('All Calories: ' + str(maxCalories))
			break
		if line == '\n':
			maxCalories.append(currCalories)
			currCalories = 0;
		else:
			currCalories += int(line)