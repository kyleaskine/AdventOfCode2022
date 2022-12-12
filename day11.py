import re
import copy
import math

def processMonkey(monkeys, line, f):
	monkeyID = -1
	while True:
		if not line or line == '\n':
			return
		elif re.search('^Monkey', line):
			input = line.split(':')
			input = input[0].split(' ')
			monkeyID = int(input[1])
			monkeys[monkeyID] = {}
		elif re.search('^\s+Starting', line):
			input = line.split(':')
			itemInput = input[1].split(',')
			itemArray = []
			for item in itemInput:
				itemArray.append(int(item))
			monkeys[monkeyID].update({"items":itemArray})
		elif re.search('^\s+Operation', line):
			input = line.split(':')
			input = input[1].split('= ')
			input = input[1].split(' ')
			operation = []
			for item in input:
				item = re.sub('\n', '', item)
				if re.search('^\d+$', item):
					operation.append(int(item))
				else:
					operation.append(item)
			monkeys[monkeyID].update({"operation":operation})
		elif re.search('^\s+Test', line):
			input = line.split('by ')
			input = int(input[1])
			monkeys[monkeyID].update({"divisibleBy":input})
		elif re.search('^\s+If true:', line):
			input = line.split('monkey ')
			input = int(input[1])
			monkeys[monkeyID].update({"trueThrowTo":input})
		elif re.search('^\s+If false:', line):
			input = line.split('monkey ')
			input = int(input[1])
			monkeys[monkeyID].update({"falseThrowTo":input})
			monkeys[monkeyID].update({"inspected":0})
		line = f.readline()
		
def processItem(monkeys, monkey, itemID, shouldProcessRelief, mod):
	item = doOperation(monkey, itemID)
	if shouldProcessRelief:
		item = processRelief(item)
	item %= mod
	testAndThrow(monkeys, monkey, item)
	monkey['inspected'] += 1
	
def doOperation(monkey, item):
	operation = copy.deepcopy((monkey['operation']))
	if operation[0] == 'old':
		operation[0] = item
	if operation[2] == 'old':
		operation[2] = item
	if operation[1] == '+':
		return operation[0] + operation[2]
	elif operation[1] == '*':
		return operation[0] * operation[2]
	raise Exception('Check inputs: ' + operation[1])

def processRelief(item):
	return math.floor(item / 3)
	
def testAndThrow(monkeys, monkey, item):
	if item % monkey['divisibleBy'] == 0:
		throwTo(monkeys, item, monkey['trueThrowTo'])
	else:
		throwTo(monkeys, item, monkey['falseThrowTo'])
		
def throwTo(monkeys, item, monkeyID):
	monkeys[monkeyID]['items'].append(item)
	
def findSmallestMod(monkeys):
	mod = 1
	for monkey in monkeys:
		mod *= monkeys[monkey]['divisibleBy']
	return mod

with open('day11.txt') as f:
	monkeys = {}
	roundNumber = 1
	while True:
		line = f.readline()
		if not line:
			break
		elif re.search('^Monkey', line):
			processMonkey(monkeys, line, f)
	monkeysPartTwo = copy.deepcopy(monkeys)
	mod = findSmallestMod(monkeys)
	while roundNumber <= 20:
		for monkeyID in monkeys:
			for itemID in monkeys[monkeyID]['items']:
				processItem(monkeys, monkeys[monkeyID], itemID, True, mod)
			monkeys[monkeyID]['items'] = []
		roundNumber += 1
	part1 = []
	for monkeyID in monkeys:
		part1.append(monkeys[monkeyID]['inspected'])
	part1.sort(reverse=True)
	print('Part 1: ' + str(part1[0] * part1[1]))
	
	monkeys = monkeysPartTwo
	roundNumber = 1
	while roundNumber <= 10000:
		for monkeyID in monkeys:
			for itemID in monkeys[monkeyID]['items']:
				processItem(monkeys, monkeys[monkeyID], itemID, False, mod)
			monkeys[monkeyID]['items'] = []
		roundNumber += 1
	part2 = []
	for monkeyID in monkeys:
		part2.append(monkeys[monkeyID]['inspected'])
	part2.sort(reverse=True)
	print('Part 2: ' + str(part2[0] * part2[1]))