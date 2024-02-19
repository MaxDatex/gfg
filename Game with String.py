'''
Given a string s of lowercase alphabets and a number k, the task is to print the minimum value of the string after removal of k characters. 
The value of a string is defined as the sum of squares of the count of each distinct character present in the string. 
'''


import heapq

class Solution:
    def minValue(self, s, k):
        hm = {char: 0 for char in s}
        for char in s:
            hm[char] += 1
        
        vals = [-i for i in hm.values()]
        
        heapq.heapify(vals)
        for i in range(k):
            max_val = heapq.heappop(vals)
            if max_val == 0:
                return 0
            heapq.heappush(vals, max_val+1)
        return sum([i**2 for i in vals])
