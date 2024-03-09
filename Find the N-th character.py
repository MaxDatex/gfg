'''
Given a binary string s. Perform r iterations on string s, where in each iteration 0 becomes 01 and 1 becomes 10. 
Find the nth character (considering 0 based indexing) of the string after performing these r iterations (see examples for better understanding).
'''


class Solution:
    def nthCharacter(self, s, r, n):
        corr = {
            '1': '10',
            '0': '01'
        }
        
        r = 1 << r
        
        while r > 1:
            index = n // r
            s = corr[s[index]]
            if n >= r:
                n = n % r
            r = r // 2
            
        return s[n//r]
