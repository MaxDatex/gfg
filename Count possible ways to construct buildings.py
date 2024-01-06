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
