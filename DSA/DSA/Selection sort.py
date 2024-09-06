#Selection sort
def selectionSort(array, n):
	for i in range(n):
		min = i
		for j in range(i + 1, n):
			if array[j] < array[min]:
				min = j
		(array[i], array[min]) = (array[min], array[i])
arr = list(map(int,input("enter the element with sepoarated space: ").split()))
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)