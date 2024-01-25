'''
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item here. 
'''


class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        ans = 0
        l = sorted(arr, key=lambda item: item.value / item.weight, reverse=True)
        for item in l:
            if item.weight <= W:
                ans += item.value
                W -= item.weight
            elif item.weight > W:
                val = (item.value / item.weight) * W
                ans += val
                W -= val
                break
        return ans
