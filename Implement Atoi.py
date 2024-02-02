'''
Given a string, s, the objective is to convert it into integer format without utilizing any built-in functions. If the conversion is not feasible, the function should return -1.

Note: Conversion is feasible only if all characters in the string are numeric or if its first character is '-' and rest are numeric.
'''


class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        ints = list(range(ord('0'), ord('9')+1))
        i = 0
        sign = 1
        res = 0
        
        if s[0] == '-':
            sign = -1
            i += 1
        
        for char in range(i, len(s)):
            if ord(s[char]) not in ints:
                return -1
            res = res * 10 + ord(s[char]) - ord('0')
        return sign * res
