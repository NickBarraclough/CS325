############################################################################
# MERGESORT 3
# Nick Barraclough
# Description: Read integers from a file, spit the data recursively into
#	thirds and sort each line of integers.
#	from smallest to largest.
############################################################################

import random
import time

# Merge Sort function
# Takes an array and recursively sorts its elements
def mergeSort3(array):

	if len(array) > 1:

		midL = len(array) // 3
		midR = len(array) // 3 + 1
		left = array[:midL]
		right = array[midL:2*(midL+1)-1]
		middle = array[2*(midL+1)-1:]

		# Recursive calls to split the array until elements are singled out
		mergeSort3(left)
		mergeSort3(middle)
		mergeSort3(right)	
#-- MERGE PORTION, should be Θ(n)
		l = m = r = idx = 0
		
		while l < len(left) and r < len(right) and m < len(middle):
			if left[l] <= middle[m] and left[l] <= right[r]:
				array[idx] = left[l]
				l += 1
			elif middle[m] <= left[l] and middle[m] <= right[r]:
				array[idx] = middle[m]
				m += 1
			elif right[r] <= middle[m] and right[r] <= left[l]:
				array[idx] = right[r]
				r += 1
			idx = idx + 1
		
		while l < len(left) and m < len(middle):
			if(left[l] < middle[m]):
				array[idx] = left[l];
				l += 1;
			elif(left[l] >= middle[m]):
				array[idx] = middle[m];
				m += 1;
			idx += 1 

		while r < len(right) and l < len(left):
			if(right[r] < left[l]):
				array[idx] = right[r];
				r += 1;
			elif(right[r] >= left[l]):
				array[idx] = left[l];
				l += 1;
			idx += 1 

		while r < len(right) and m < len(middle):
			if(right[r] < middle[m]):
				array[idx] = right[r];
				r += 1;
			elif(right[r] >= middle[m]):
				array[idx] = middle[m];
				m += 1;
			idx += 1 


		while l < len(left):
	
			array[idx] = left[l]
			l = l + 1
			idx = idx + 1
	
		while m < len(middle) and idx < len(array):
			array[idx] = middle[m]
			m += 1
			idx += 1
	
		while r < len(right):
	
			array[idx] = right[r]
			r = r + 1
			idx = idx + 1
	
	return array
	
	
###############################################################################

def main():
	
	array = []
	length = int(input("\nHow many integers should be generated and sorted?: "))	
	for row in range(length):
		value = random.randint(0,10000)
		array.append(value)

	start = time.time()
	mergeSort3(array)

	print("\nNumber of integers: ", len(array))
	print("Amount of time to sort integers: ", time.time() - start, "\n")

if __name__ == "__main__":

	main()

###############################################################################


