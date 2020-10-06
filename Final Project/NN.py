# Nearest Neighbor Algorithm for TSP

import sys, math, time, random

start = time.time()

# Read points in from file, populate array of points
with open(sys.argv[1], 'r') as inFile:
	numLines = 0
	for line in inFile.readlines(): numLines += 1
	Points = [[0 for i in range(2)] for j in range(numLines)]
	Cities = [i for i in range(numLines)]
	inFile.close()
with open(sys.argv[1], 'r') as inFile:
	for line in range(numLines):
		coordinate = inFile.readline().split()		# to populate Points list
		Points[line][0] = int(coordinate[1])
		Points[line][1] = int(coordinate[2])

# CALCULATE DISTANCE BETWEEN 2 POINTS
def calcDistance(Point1, Point2):
	distance = math.sqrt(((int(Point1[0]) - int(Point2[0]))**2) + ((int(Point1[1]) - int(Point2[1]))**2))
	return distance

# Populate adjacency matrix of all edge weights
Weights = [[0 for i in range(numLines)] for j in range(numLines)]
for i in range(numLines):			# Construct Weights matrix for all
    nodeA = Points[i]				# possible edges
    for j in range(numLines):
        nodeB = Points[j]
        if i == j:
            Weights[i][j] = 99999999  # To be ignored later
        else:   # ROUND DISTANCE FROM nodeA TO nodeB TO NEAREST INTEGER
            Weights[i][j] = round(calcDistance(nodeA, nodeB))

totalDistance = 0
minDistance = 99999999
visited = [0 for x in range(numLines)]
randStart = random.randrange(numLines)
#visited[0] = 1
visited[randStart] = 1
#Path = [0 for x in range(numLines)]
Path = []
#Path.append(0)
Path.append(randStart)
pathCounter = 1
for i in range(1,numLines):
	for j in range(0,numLines):
#	for j in range(1,numLines):
		if visited[j] != 1:
			if Weights[Path[i-1]][j] < minDistance:
				minDistance = Weights[Path[i-1]][j]
				lowest = j

	visited[lowest] = 1               # Mark city as visited
	Path.append(lowest)               # Add city to tour
	pathCounter += 1
	if minDistance != 99999999:       # Ignore when minDistance is not updated
		totalDistance += minDistance  # Add distance for current edge
	minDistance = 99999999            # Revert minDistance to find next lowest edge in the set

# Add distance from last city to first
lastWeight = Weights[Path[numLines - 1]][Path[0]]
totalDistance += lastWeight

print("Tour Length: ", totalDistance)

# Create or Overwrite Output File
splat = sys.argv[1] + ".tour"         # Create a string that appends ".tour" to the input file
outFile = open(splat, 'w')            # Open the [*].tour file for writing
outFile.write(str(int(totalDistance)))# First line of output file is the distance of the tour
outFile.write("\n")
for i in range(numLines):             # Remaining lines are the city
    outFile.write(str(Path[i]))       # identifiers in the order of the tour
    outFile.write("\n")

finish = time.time() - start
print("Running Time: ", finish)
