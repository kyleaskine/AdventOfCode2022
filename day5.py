import copy
with open('day5.txt') as f:
	stack = []
	while True:
		line = f.readline()
		if line == '\n':
			break
		i = 0;
		while True:
			if i == len(line):
				break;
			if len(stack) <= i//4:
				stack.append([])
			if line[i] == '[':
				stack[i//4].insert(0,line[i+1])
			i += 4
	print(stack)
	
	queue = copy.deepcopy(stack)
	while True:
		line = f.readline()
		if not line:
			break
		i = 5
		chars = ''
		while line[i] != ' ':
			chars += line[i]
			i += 1
		numMoved = int(chars)
		chars = ''
		i += 6
		while line[i] != ' ':
			chars += line[i]
			i += 1
		startPosition = int(chars) - 1
		chars = ''
		i += 4
		while line[i] != '\n':
			chars += line[i]
			i += 1
		endPosition = int(chars) - 1
		
		while numMoved > 0:
			stack[endPosition].append(stack[startPosition].pop())
			queue[endPosition].append(queue[startPosition].pop(len(queue[startPosition]) - numMoved))
			numMoved -= 1
	i = 0
	while i < len(queue):
		print(queue[i].pop(), end = '')
		i += 1
	i = 0
	print()
	while i < len(stack):
		print(stack[i].pop(), end = '')
		i += 1