###########################################################################
# Euclidean Minimum Spanning Tree
# Author: Nicolas Barraclough
# Description: Reads in a "graph.txt" file with coordinates for a weighted,
#				undirected graph. Then calculates the edges and edge
#				weights for a MST of the graph set. Also displays the total
#				weight of the MST.
###########################################################################

import sys
import math

def calcDistance(Point1, Point2):
	distance = math.sqrt(((int(Point1[0]) - int(Point2[0]))**2) + ((int(Point1[1]) - int(Point2[1]))**2)) 
	return distance

with open(sys.argv[1], 'r') as inFile:
	numLines = int(inFile.readline().strip())		# Read first line for number of coordinates
	Points = [[0 for i in range(2)] for j in range(numLines)]

	for line in range(numLines):					# Read remaining lines
		coordinate = inFile.readline().split()		# to populate Points
		Points[line][0] = int(coordinate[0])		
		Points[line][1] = int(coordinate[1])

Weights = [[0 for i in range(numLines)] for j in range(numLines)]
for i in range(numLines):			# Construct Weights matrix for all
	nodeA = Points[i]				# possible edges
	for j in range(numLines):
		nodeB = Points[j]
		Weights[i][j] = calcDistance(nodeA, nodeB)
for i in range(numLines):
	Weights[i][i] = -1				# weights between the same exact node
	
key = [999999 for i in range(numLines)]		#set all keys to "infinity"
key[0] = 0
p = [0 for i in range(numLines)]
minSet = [0 for i in range(numLines)]
index = 0

for i in range(numLines - 1):					# Finding the minimum next
	_min = 10000								# key and update the minimum
	for j in range(numLines):					# Set to note that this
		if minSet[j] == 0 and key[j] < _min:	# edge has been used before
			_min = key[j]
			index = j
	u = index
	minSet[u] = 1
	for j in range(numLines):
		if Weights[u][j]:						# if it's an edge
			if minSet[j] == 0:					# and not in the set
				if Weights[u][j] < key[j]:		# and the weight is 
					p[j] = u					# less than the key
					key[j] = Weights[u][j]
total = 0

print("Edges in MST")							# Print the results of the
print("Point (x,y)\t\t\tDistance")				# program
for i in range(numLines - 1):
	print("   ", Points[p[i + 1]], "-", Points[i + 1], "\t\t", int(Weights[i + 1][p[i + 1]]))
	total += int(Weights[i + 1][p[i + 1]])
print("\tTotal Distance: ", total)	
	


