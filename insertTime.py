############################################################################
# INSERTION SORT
# Nick Barraclough
# Description: Generate n random ints and sort the integers
#	from smallest to largest. Outputs the time it took to sort.
############################################################################

import random
import time

# Insertion Sort function
# Takes an array and iterates through, moving smaller values before larger ones
def insertionSort(array):

	for i in range(1, len(array)):

		value = array[i]
		idx = i - 1

		while idx >= 0 and array[idx] > value:

			array[idx + 1] = array[idx]
			idx = idx - 1

		array[idx + 1] = value

	return array


##############################################################################

def main():

	array = []
	length = int(input("\nHow many integers should we generate and sort?: "))

	for row in range(length):
		
		value = random.randint(0, 10000)

		array.append(value)

	start = time.time()
	insertionSort(array)

	print("\nNumber of integers: ", len(array))
	print("Amount of time to sort integers: ", time.time() - start, "\n")

if __name__ == "__main__":

	main()

##############################################################################
