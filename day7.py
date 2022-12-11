import re

def buildFS(f):
	root = {}
	while True:
		line = f.readline()
		if not line:
			return root
		elif re.search('^dir', line):
			dirName = re.search('^dir (\w+)$', line).group(1)
			root[dirName] = {}
		elif re.search('^[0-9]+', line):
			size = int(re.search('^([0-9]+)', line).group(1))
			name = re.search('^[0-9]+ (.+)', line).group(1)
			root[name] = size
		elif re.search('^\$ cd', line):
			name = re.search('^\$ cd (.+)', line).group(1)
			if name == '..':
				return root
			else:
				line = f.readline()
				if line != '$ ls\n':
					raise Exception('Look at input ' + line)
				root.update({name: buildFS(f)})

def getTotalSizeDirsLessThanX(root, sizeLimit):
	sum = 0;
	size = 0;
	for key in root:
		if type(root[key]) is dict:
			temp = getTotalSizeDirsLessThanX(root[key], sizeLimit)
			sum += temp[0]
			size += temp[1]
		else:
			size += root[key]
	if size <= sizeLimit:
		sum += size
	return [sum,size]
	
def getSmallestDirectorySizeLessThanX(root, sizeLimit):
	smallest = 1000000000
	size = 0
	for key in root:
		if type(root[key]) is dict:
			temp = getSmallestDirectorySizeLessThanX(root[key], sizeLimit)
			if(temp[0] < smallest):
				smallest = temp[0]
			size += temp[1]
		else:
			size += root[key]
	if size >= sizeLimit and size < smallest:
		smallest = size
	#print(root)
	#print([smallest,size])
	return [smallest,size]

with open('day7.txt') as f:
	root = {}
	while True:
		line = f.readline()
		if not line:
			break
		elif re.search('^\$ ls', line):
			root = buildFS(f)
			print(root)
	dirs = getTotalSizeDirsLessThanX(root, 100000)
	print(dirs)
	print(getSmallestDirectorySizeLessThanX(root, 30000000 - (70000000 - dirs[1])))