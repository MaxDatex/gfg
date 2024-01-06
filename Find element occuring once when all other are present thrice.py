'''
Given an array of integers arr[] of length N, every element appears thrice except for one which occurs once.
Find that element which occurs once.
'''


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
        return ans
