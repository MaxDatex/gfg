'''
Given an array arr[] of length n. Find all possible unique permutations of the array in sorted order. 
A sequence A is greater than sequence B if there is an index i for which Aj = Bj for all j<i and Ai > Bi.
'''


def unique(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item
        
        
def permute(arr):
    res = []
    if len(arr) == 1:
        return [arr[:]]
        
    for i in range(len(arr)):
        num = arr.pop(0)
        perms = permute(arr)
        
        for perm in perms:
            perm.append(num)
        
        res.extend(perms)
        arr.append(num)
    return res
    

class Solution:
    def uniquePerms(self, arr, n):
        perms = permute(arr)
        res = list(unique(sorted(perms)))
            
        return res
