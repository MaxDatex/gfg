'''
Given an array of integers nums and a number k, write a function that returns true if given array can be divided into pairs such that sum of every pair is divisible by k.
'''


from collections import defaultdict

class Solution:
	def canPair(self, nuns, k):
        size = len(nuns)
        
        if size % 2 != 0:
            return False
            
        hashmap = defaultdict(lambda: 0)
        
        for i in range(size):
            rem = nuns[i] % k
            hashmap[rem] += 1
            
        for i in range(size):
            rem = nuns[i] % k
            
            if 2 * rem == k:
                if hashmap[rem] % 2 != 0:
                    return False
                    
            elif rem == 0:
                if hashmap[rem] % 2 != 0:
                    return False
                    
        	else:
        	    if hashmap[rem] != hashmap[k-rem]:
                    return False
                
        return True
