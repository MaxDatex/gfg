'''
Given a string S consisting of the characters 0, 1 and 2. 
Your task is to find the length of the smallest substring of string S that contains all the three characters 0, 1 and 2. 
If no such substring exists, then return -1.
'''


class Solution:
    def smallestSubstring(self, S):
        zero = -1
        one = -1
        two = -1
        ans=float('inf')
        for i in range(len(S)):
            if S[i] == '0': zero=i
            elif S[i] == '1': one = i
            elif S[i] == '2': two = i
            if zero != -1 and one != -1 and two != -1:
                temp = max(zero, one, two) + 1 - min(zero, one, two)
                ans=min(ans,temp)
        if ans!= float('inf'):
            return ans
        return -1
