'''
Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

    enqueue(x) : Add an item x to rear of queue
    dequeue() : Remove an item from front of queue
    size() : Returns number of elements in queue.
    front() : Finds front item.
'''


from collections import deque
#Function to reverse first k elements of a queue.
class Solution:
    def modifyQueue(self, q, k):
        q = deque(q) # queue
        tmp = [] # stack
        for i in range(k):
            tmp.append(q.popleft())
            
        for i in range(k):
            q.append(tmp.pop())
            
        for i in range(len(q) - k):
            q.append(q.popleft())
        
        return q
