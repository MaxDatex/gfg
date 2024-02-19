'''
A function F is defined as follows F(n)= (1) +(2*3) + (4*5*6) ... upto n terms (look at the examples for better clarity). Given an integer n, determine the F(n).

Note: As the answer can be very large, return the answer modulo 109+7.
'''


class Solution:
    def sequence(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        ans = 1
        j = 2
        for i in range(2, n+1):
            temp = 1
            for _ in range(i):
                temp *= j
                j += 1
   
            ans = (ans + temp) % (10**9+7)
        return ans
