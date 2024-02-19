'''
Given an integer n, return the first n elements of Recaman’s sequence.
It is a function with domain and co-domain as whole numbers. It is recursively defined as below:
Specifically, let a(n) denote the (n+1)th term. (0 being the 1st term).
The rule says:
a(0) = 0
a(n) = a(n-1) - n, if a(n-1) - n > 0 and is not included in the sequence previously
       =  a(n-1) + n otherwise. 
'''

class Solution:
    def recamanSequence(self, n):
        # code here
        if n < 2: 
            return [i for i in range(n)] 
        visited = {0, 1}
        sequence = [0, 1] 
        current = 1 
        for i in range(2, n + 1): 
            current = current - i if current - i >= 0 and current - i not in visited else current + i
            visited.add(current)
            sequence.append(current) 
        return sequence
