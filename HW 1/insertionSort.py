############################################################################
# INSERTION SORT
# Nick Barraclough
# Description: Read integers from a file and sort each line of integers
#	from smallest to largest.
############################################################################


# Insertion Sort function
# Takes an array and iterates through, moving smaller values before larger ones
def insertionSort(array):

	for i in range(1, len(array)):

		value = array[i]
		idx = i - 1

		while idx >= 0 and array[idx] > value:

			array[idx + 1] = array[idx]
			idx = idx - 1

		array[idx + 1] = value;

	return array


##############################################################################

def main():

	data = open("data.txt", "r")
	sorted = open("insert.out", "w")

	for row in data:

		row = list(map(int, row.split()))
		sorted.write(' '.join(map(str, insertionSort(row[1:]))))
		sorted.write('\n')

	data.close()
	sorted.close()

if __name__ == "__main__":

	main()

##############################################################################
