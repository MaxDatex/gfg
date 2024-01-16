'''
Given two integers m and n, try making a special sequence of numbers seq of length n such that

    seqi+1 >= 2*seqi 
    seqi > 0
    seqi <= m

'''


class Solution:
    def numberSequence(self, m, n):
        if m < n: return 0
        if n == 0: return 1
        
        return self.numberSequence(m/2, n-1) + self.numberSequence(m-1, n)
            
