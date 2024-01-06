'''
Given an array of integers arr[] of length N, every element appears thrice except for one which occurs once.
Find that element which occurs once.
'''

# Works only for positive numbers
class Solution:
    def singleElement(self, arr, N):
        
        ans = 0
        
        for i in range(32):
            count = 0
            for elem in arr:
                elem = elem >> i
                if elem & 1 == 1:
                    count += 1
            if count % 3 == 1:
                ans += 1 << i
        return and

# ==================================

class Solution:
    def singleElement(self, arr, N):
        arr.sort()
        
        for i in range(0, N-2, 3):
            if arr[i] != arr[i+2]:
                return arr[i]
        return arr[N-1]
