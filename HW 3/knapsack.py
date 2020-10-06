#########################################################################
# Nick Barraclough
# CS325 Analysis of Algorithms
# 2/7/2020
# Homework 3 Problem 3  - 0/1 Knapsack: Recursive vs Dynamic Programming
#########################################################################

import random
import time

# RECURSIVE ALGORITHM
def recKnapsack(val, wt, W, n):
	if n == 0 or W == 0:	# cover Base Case
		return 0
	if (wt[n - 1] > W):		# current item is too heavy
		return recKnapsack(val, wt, W, n - 1) 
	else:	# take the max between choosing the item, and not choosing it
		return max(val[n - 1] + recKnapsack(val, wt, W - wt[n - 1], n - 1), recKnapsack(val, wt, W, n - 1))
	
# DYNAMIC PROGRAMMING ALGORITHM
def dpKnapsack(val, wt, W, n):
	sack = [[0 for j in range(W + 1)] for i in range(n + 1)]	
	for i in range(n + 1):
		for j in range(W + 1):
			if i == 0 or j == 0:
				sack[i][j] = 0		# 0 item column and no item 
			elif wt[i - 1] <= j:
				sack[i][j] = max(sack[i - 1][j - wt[i - 1]] + val[i - 1], sack[i - 1][j])
			else:
				sack[i][j] = sack[i - 1][j]
	return sack[n][W]


def main():

	n = 30
	W = 100
	while n < 80:

		val = []						# populate item values
		for i in range(n):
			value = random.randint(0,100)
			val.append(value)

		wt = []							# populate item weights
		for i in range(n):
			weight = random.randint(0,W)
			wt.append(weight)
	
		start = time.time()
		maxRec = recKnapsack(val, wt, W, n)
		recTime = time.time() - start

		begin = time.time()
		maxDP = dpKnapsack(val, wt, W, n)
		dpTime = time.time() - begin

		print("N=", n, " W=", W, " Rec time =", recTime, "\tDP time =", dpTime, "\tmax Rec =", maxRec, "\tmax DP =", maxDP)
		
		n += 5

if __name__ == "__main__":

	main()



