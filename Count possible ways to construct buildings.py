'''
There is a road passing through a city with N plots on both sides of the road. 
Plots are arranged in a straight line on either side of the road. 
Determine the total number of ways to construct buildings in these plots, ensuring that no two buildings are adjacent to each other. 
Specifically, buildings on opposite sides of the road cannot be adjacent.

Using * to represent a plot and || for the road, the arrangement for N = 3 can be visualized as follows: * * * || * * *.

Note: As the answer can be very large, print it mod 109+7.
'''


class Solution:
    def TotalWays(self, N):
        if N == 1:
            return 4
        if N == 2:
            return 9
            
        data = [2, 3]
        mod = 10**9 + 7
        
        for i in range(2, N):
            data.append((data[i-1] + data[i-2]) % mod)
        
        return int(data[-1] ** 2) % mod
