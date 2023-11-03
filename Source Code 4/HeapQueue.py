import heapq

# initialize the list
li = [5, 7, 9, 1, 3]
print('Initialize the list : ', li)

# transform list into a heap
heapq.heapify(li)
print ('The created heap from list : ', list(li))

# push 4 into heap
heapq.heappush(li, 4)
print('The modified heap after push 4 : ', end="")
print(list(li))

# push 6 and pop items simultaneously from heap
# print('The popped item using heappushpop() : ', end="")
# print(heapq.heappushpop(li, 6))

# push 2 and pop items simultaneously from heap
# print('The popped item using heapreplace() : ', end="")
# print(heapq.heapreplace(li, 2))

# pop elements from heap
print('Pop all elements from heap : ', end=" ")
for i in range(len(li)): 
    print(heapq.heappop(li), end=" ")