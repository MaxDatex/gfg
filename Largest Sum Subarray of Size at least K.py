'''
Given an array a of length n and a number k, find the largest sum of the subarray containing at least k numbers. 
It is guaranteed that the size of array is at-least k.
'''


class Solution():
    def maxSumWithK(self, a, n, k):
        l, r = 0, 0
        max_sum = float('-inf')
        curr_sum = 0
        last = 0
        
        while r < n:
            curr_sum += a[r]
            if r - l + 1 == k:
                max_sum = max(max_sum, curr_sum)
            elif r - l + 1 > k:
                last += a[l]
                l += 1
                
                if last < 0:
                    curr_sum -= last
                    last = 0
                max_sum = max(max_sum, curr_sum)
            r += 1
            
        return max_sum
