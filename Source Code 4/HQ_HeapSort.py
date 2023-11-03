import heapq

# Function to perform the sorting using
# heaop sort
def heap_sort(arr):
	heapq.heapify(arr)
	result = []
	while arr:
		result.append(heapq.heappop(arr))
	return result

# Driver Code
arr = [60, 20, 40, 70, 30, 10]
print("Input Array: ", arr)
print("Sorted Array: ", heap_sort(arr))