#########################################################################
# Nick Barraclough
# CS325 Analysis of Algorithms
# 2/7/2020
# Homework 3 Problem 4  -  Shopping Spree
#########################################################################

def main():
	inFile = open("shopping.txt", "r")
	outFile = open("results.txt", "w")

	T = int(inFile.readline())
	for testcases in range(T):

		N = int(inFile.readline())
		dictionary = dict()	#Create a dictionary

		# For each item, populate the dictionary with its price & weight, and keep track of the index each item is at
		idx = 1		# items will start at index 1
		for items in range(N):
			P, W = map(int, inFile.readline().split())
			dictionary[P] = [W, idx]
			idx += 1	

		# Create a list of family member weight capacities
		weights = []
		F = int(inFile.readline())
		for M in range(F):
			weights.append(int(inFile.readline()))
		

		itemsToPick = []
		values = []
		for w in weights:
			itemPrices = sorted(dictionary.keys())[::-1] # Make a view object with item prices sorted in reverse order
			cost = 0
			temp = []
			for i in range(len(dictionary)):
				arr = []
				x = 0
				price = 0
				if dictionary[itemPrices[i]][0] <= w:
					x = dictionary[itemPrices[i]][0]
					price = itemPrices[i]
					arr += dictionary[itemPrices[i]][1],
				for j in range(i + 1, len(dictionary)):
					if dictionary[itemPrices[j]][0] + x <= w:
						x += dictionary[itemPrices[j]][0]
						price += itemPrices[j]
						arr += dictionary[itemPrices[j]][1],
				if cost < price:
					cost = price
					temp = arr
					temp.sort()
					itemsToPick.append(temp)
					values.append(cost)

		# Output current Test Case and its results
		outFile.write("Test Case %d\n"%(testcases + 1))
		outFile.write("Total Price: %d\n"%(sum(values)))
		outFile.write("Member Items\n")
		for i in range(len(itemsToPick)):
			outFile.write("%d: %s"%(i + 1, " ".join(map(str, itemsToPick[i]))))
			outFile.write("\n")
		outFile.write("\n")

	inFile.close()
	outFile.close()

if __name__ == "__main__":

	main()
