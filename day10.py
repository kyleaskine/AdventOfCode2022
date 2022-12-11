import re

def isLit (cycles, register):
	pixel = (cycles - 1) % 40
	if pixel - 1 == register or pixel == register or pixel + 1 == register:
		return True
	return False
	
def writePixel (cycles, register):
	if isLit(cycles, register):
		return '#'
	return '.'

with open('day10.txt') as f:
	cycles = 0
	register = 1
	crtOutput = ''
	signalHistory = []
	while True:
		line = f.readline()
		xToAdd = 0
		if not line or line == '\n':
			print(crtOutput)
			print(signalHistory[19] + signalHistory[59] + signalHistory[99] + signalHistory[139] + signalHistory[179] + signalHistory[219])
			break
		elif re.search('^noop', line):
			cycles += 1
		elif re.search('^addx', line):
			spl = line.split(' ')
			xToAdd = int(spl[1])
			cycles += 1
		if cycles % 40 == 1 and crtOutput != '':
			print(crtOutput)
			crtOutput = ''
		crtOutput += writePixel(cycles, register)
		signalHistory.append(register * cycles)
		if xToAdd != 0:
			cycles += 1
			signalHistory.append(register * cycles) #has to be before the register change because we measure during cycle, not after
			if cycles % 40 == 1:
				print(crtOutput)
				crtOutput = ''
			crtOutput += writePixel(cycles, register)
			register += xToAdd
			
		
	
	
