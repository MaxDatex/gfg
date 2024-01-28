'''
Given a string str consisting of digits, you can divide it into sub-groups by separating the string into substrings. 
For example, "112" can be divided as {"1", "1", "2"}, {"11", "2"}, {"1", "12"}, and {"112"}.

A valid grouping can be done if you are able to divide sub-groups where the sum of digits in a sub-group is less 
than the sum of the digits of the sub-group immediately right to it. 
Your task is to determine the total number of valid groupings that could be done for a given string.
'''


class Solution:
	def TotalCount(self, s):
		length = len(s)
		summ = sum(int(i) for i in s)
		
		dp = [[-1 for _ in range(summ+1)] for _ in range(length+1)]
		
		return self.group(length, 0, 0, s, dp)
		
	def group(self, length, idx, initialsum, s, dp):
	    if idx == length:
	        return 1
	        
	    if dp[idx][initialsum] != -1:
	        return dp[idx][initialsum]
	        
	    cursum = 0
	    ans = 0
	    for i in range(idx, length):
	        cursum += int(s[i])
	        if cursum >= initialsum:
	            ans += self.group(length, i+1, cursum, s, dp)
        dp[idx][initialsum] = ans
        return ans
