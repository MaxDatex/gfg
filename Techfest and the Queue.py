'''
A Techfest is underway, and each participant is given a ticket with a unique number. 
Organizers decide to award prize points to everyone who has a ticket ID between a and b (inclusive). 
The points given to a participant with ticket number x will be the sum of powers of the prime factors of x.

For instance, if points are to be awarded to a participant with ticket number 12, 
the amount of points given out will be equal to the sum of powers in the prime factorization of 12 (2^2 × 3^1), 
which will be 2 + 1 = 3.

Given a and b, determine the sum of all the points that will be awarded to the participants with ticket numbers between a and b (inclusive).
'''


from typing import List
from collections import defaultdict


class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        factors = list(range(b+1))
        i = 2
        
        while i*i <= b:
            if factors[i] == i:
                for j in range(i*i, b+1, i):
                    factors[j] = i
            i += 1
        
        winners = list(range(a, b+1))
        ans = 0
        
        for i in winners:
            factor = defaultdict(int)

            while i > 1:
                factor[factors[i]] += 1
                i //= factors[i] 
            
            ans += sum(factor.values())
            
        return ans
