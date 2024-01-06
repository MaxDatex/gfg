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
