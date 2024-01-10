'''
Given an array arr containing N integers and a positive integer K, 
find the length of the longest sub array with sum of the elements divisible by the given value K.
'''


class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
		# Bruteforce
		ans = 0
		pfs = [0 for _ in range(n+1)]
        for i in range(n):
            pfs[i+1] = pfs[i] + arr[i]
            
        for i in range(n-1):
        	    for j in range(i+1, n):
        	        el_sum = pfs[j+1]-pfs[i]
        	        if el_sum % K == 0:
        	            length = j - i + 1
        	            ans = max(length, ans)
        # return ans

        # O(n)
        from collections import defaultdict
        
        pfs, ans = 0, 0
        idx = defaultdict(int)
        idx[0] = -1
        
        for i in range(n):
            pfs += arr[i]
            rem = pfs % K
            if rem in idx:
                ans = max(ans, i - idx[rem])
            else:
                idx[rem] = i
        return ans
