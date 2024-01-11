'''
Given a non-negative integer S represented as a string, 
remove K digits from the number so that the new number is the smallest possible.
Note : The given num does not contain any leading zero.
'''


class Solution:

    def removeKdigits(self, S, K):
        stack = []
        
        for c in S:
            while stack and stack[-1] > c and K > 0:
                stack.pop()
                K -= 1
            
            if stack or c != '0':
                stack.append(c)
            
        while stack and K > 0:
            stack.pop()
            K -= 1
            
        return ''.join(stack) if stack else '0'
