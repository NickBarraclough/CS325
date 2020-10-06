############################################################################
# MERGE SORT
# Nick Barraclough
# Description: Create an array of numbers between 0 and 10,000 and sort 
#	 integers from smallest to largest.
############################################################################

import random
import time

# Merge Sort function
# Takes an array and recursively sorts its elements
def mergeSort(array):

	if len(array) > 1:


		middle = len(array) // 2
		left = array[:middle]
		right = array[middle:]

		# Recursive calls to split the array until elements are singled out
		mergeSort(left)
		mergeSort(right)

		l = r = idx = 0

		while l < len(left) and r < len(right):
			
			if left[l] < right[r]:

				array[idx] = left[l]
				l = l + 1

			else:

				array[idx] = right[r]
				r = r + 1

			idx = idx + 1

		while l < len(left):

			array[idx] = left[l]
			l = l + 1
			idx = idx + 1

		while r < len(right):

			array[idx] = right[r]
			r = r + 1
			idx = idx + 1

		return array




##################################################################################

def main():

	array = []
	length = int(input("\nHow many integers should we generate and sort?: "))

	for row in range(length):
		
		value = random.randint(0, 10000)

		array.append(value)

	start = time.time()
	mergeSort(array)

	print("\nNumber of integers: ", len(array))
	print("Amount of time to sort integers: ", time.time() - start, "\n")

if __name__ == "__main__":

	main()

##################################################################################


