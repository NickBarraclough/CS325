# Branch and Bound Algorithm for TSP

import sys, math, time

# Calculate distance between two points
def calcDistance(Point1, Point2):
	distance = math.sqrt(((int(Point1[0]) - int(Point2[0]))**2) + ((int(Point1[1]) - int(Point2[1]))**2))
	return distance

# Round num to nearest integer
def nearestInt(num):
	rnd = 0.5
	flooredNum = math.floor(num)
	if ((num - rnd) < flooredNum):
		num = flooredNum
	else:
		num = flooredNum + 1
	return num

# Find minimum weighted edge
def findMinWeight(w):
	start = float('inf')
	for i in range(numLines):
		for j in range(numLines):
			if (w[i][j] != -1):
				if (start > w[i][j]):
					start = j
	return start

# Copy current solution to the final solution
def updateFinal(currPath):
	finalPath[:numLines + 1] = currPath[:]
	finalPath[numLines] = currPath[0]

# Find the minimum edge weight with a leaf of i
def firstMin(matrix, i):
	min = float('inf')
	for k in range(numLines):
		if matrix[i][k] < min and i != k:
			min = matrix[i][k]
	return min

# Find the second minimum edge weight with a leaf of i
def secondMin(matrix, i):
	first = float('inf')
	second = float('inf')
	for j in range(numLines):
		if i == j:
			continue
		if matrix[i][j] <= first:
			second = first
			first = matrix[i][j]
		elif (matrix[i][j] <= second and
			matrix[i][j] != first):
			second = matrix[i][j]
	return second

def TSPRec(matrix, currBound, currWeight, level, currPath, visited):
	if level == numLines:	# Base case, all nodes covered
		if matrix[currPath[level - 1]][currPath[findMinWeight(Weights)]] != 0:
			currResult = currWeight + matrix[currPath[level - 1]][currPath[findMinWeight(Weights)]]
			if currResult < finalResult:
				updateFinal(currPath)
				finalResult = currResult
		return

	for i in range(numLines):
		if (matrix[currPath[level-1]][i] != 0 and visited[i] == 0):
			temp = currBound
			currWeight += matrix[currPath[level - 1]][i]
			if (level==1):
				currBound -= ((secondMin(matrix, currPath[level-1]) + secondMin(matrix, i))/2);
			else:
				currBound -= ((firstMin(matrix, currPath[level-1]) + secondMin(matrix, i))/2);
			if currBound + currWeight < finalResult:
				currPath[level] = i
				visited[i] = 1
				TSPRec(matrix, currBound, currWeight, level + 1, currPath, visited)

			currWeight -= matrix[currPath[level - 1]][i]
			currBound = temp

			visited = [0 for x in range(len(visited))]
			for j in range(level):
				if currPath[j] != -1:
					visited[currPath[j]] = 1

def TSP(matrix): #Final path setup

	currBound = 0
	currPath = [-1 for x in range(numLines + 1)]
	visited = [0 for x in range(numLines)]

	for i in range(numLines):
		currBound += (firstMin(matrix, i) + secondMin(matrix, i))
	currBound = round(currBound)

	visited[findMinWeight(Weights)] = 1
	currPath[0] = findMinWeight(Weights)

	TSPRec(matrix, currBound, 0, 1, currPath, visited)

#def main

# Read points in from file, populate array of points
with open(sys.argv[1], 'r') as inFile:
	numLines = 0
	for line in inFile.readlines(): numLines += 1
	Points = [[0 for i in range(2)] for j in range(numLines)]
	Cities = [i for i in range(numLines)]
	inFile.close()
with open(sys.argv[1], 'r') as inFile:
	for line in range(numLines):
		coordinate = inFile.readline().split()		# to populate Points
		Points[line][0] = int(coordinate[1])
		Points[line][1] = int(coordinate[2])

# Populate matrixacency matrix of all edge weights
Weights = [[0 for i in range(numLines)] for j in range(numLines)]
for i in range(numLines):			# Construct Weights matrix for all
	nodeA = Points[i]				# possible edges
	for j in range(numLines):
		nodeB = Points[j]
		Weights[i][j] = calcDistance(nodeA, nodeB)
for i in range(numLines):
	Weights[i][i] = -1				# weights between the same exact node

for i in range(numLines):
	for j in range(numLines):
		Weights[i][j] = nearestInt(Weights[i][j])

finalPath = [None for x in range(numLines + 1)]
visited = [0 for x in range(numLines)]
finalResult = float('inf')

TSP(Weights)

print(finalResult)
for i in range(numLines + 1):
	print(finalPath[i], end = ' ')
print()
