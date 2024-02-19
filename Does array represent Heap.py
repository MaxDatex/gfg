'''
Given an array arr of size n, the task is to check if the given array can be a level order representation of a Max Heap.
'''


class Solution:
    def isMaxHeap(self,arr,n):
        for i in range(n//2):
            if i == n//2-1 and n%2==0:
                return arr[i] >= arr[i*2+1]
            if arr[i] < arr[i*2+1] or arr[i] < arr[i*2+2]:
                return 0
        return 1
