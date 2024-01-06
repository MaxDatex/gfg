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
