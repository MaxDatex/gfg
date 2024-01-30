'''
Given 3 strings A, B and C, the task is to find the length of the longest sub-sequence that is common in all the three given strings.
'''


class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        dp = [[[-1 for _ in range(n3+1)] for _ in range(n2+1)] for _ in range(n1+1)]
        
        def lcs(A, B, C, n1, n2, n3, dp):
            if n1 == 0 or n2 == 0 or n3 == 0:
                return 0
            if dp[n1][n2][n3] != -1:
                return dp[n1][n2][n3]
            if A[n1-1] == B[n2-1] == C[n3-1]:
                dp[n1][n2][n3] =  1 + lcs(A, B, C, n1-1, n2-1, n3-1, dp)
                return dp[n1][n2][n3]
                
            dp[n1][n2][n3] = max(lcs(A, B, C, n1-1, n2, n3, dp), 
                                lcs(A, B, C, n1, n2-1, n3, dp),
                                lcs(A, B, C, n1, n2, n3-1, dp))
            return dp[n1][n2][n3]
        
        return lcs(A, B, C, n1, n2, n3, dp)
