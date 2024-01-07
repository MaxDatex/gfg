'''
Given an array arr[] of N elements and a number K., 
split the given array into K subarrays such that the maximum subarray sum achievable out of K subarrays formed is minimum possible. 
Find that possible subarray sum.
'''


class Solution:
    def splitArray(self, arr, N, K):
        low = max(arr)
        high = sum(arr)
        
        while low < high:
            mid = (low + high) // 2
            currsum = 0
            cnt = 0
            
            for el in arr:
                currsum += el
                if currsum > mid:
                    currsum = el
                    cnt += 1
            if cnt >= K:
                low = mid + 1
            else:
                high = mid
        return high
