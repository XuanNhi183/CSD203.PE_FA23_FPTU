import heapq

class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	def isEmpty(self):
		return len(self.queue) == 0

	# for inserting an element into the queue
	def enqueue(self, data):
		self.queue.append(data)

	# for popping elements from the heap-based priority queue
	def dequeue(self):
		heapq.heapify(self.queue)
		for i in range(len(self.queue)): 
			elements = heapq.heappop(self.queue)
			return elements

if __name__ == '__main__':
	myQueue = PriorityQueue()
	myQueue.enqueue(12)
	myQueue.enqueue(1)
	myQueue.enqueue(14)
	myQueue.enqueue(7)
	myQueue.enqueue(6)
	myQueue.enqueue(2)
	print('Queue: ', myQueue)	
	print('Priority Queue: ', end=' ')	
	while not myQueue.isEmpty():
		print(myQueue.dequeue(), end=' ')