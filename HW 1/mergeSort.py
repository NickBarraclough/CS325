############################################################################
# MERGE SORT
# Nick Barraclough
# Description: Read integers from a file and sort each line of integers
#	from smallest to largest.
############################################################################


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


###############################################################################

def main():

	data = open("data.txt", "r")
	sort = open("merge.out", "w")

	for row in data:

		row = list(map(int, row.split()))
		sort.write(' '.join(map(str, mergeSort(row[1:]))))
		sort.write('\n')

	data.close()
	sort.close()

if __name__ == "__main__":

	main()

###############################################################################


