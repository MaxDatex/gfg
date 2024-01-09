'''
Given two strings, one is a text string, txt and other is a pattern string, pat. 
The task is to print the indexes of all the occurences of pattern string in the text string. 
Use one-based indexing while returing the indices. 
Note: Return an empty list incase of no occurences of pattern. Driver will print -1 in this case.
'''


class Solution:
    def search(self, pat, txt):
        N = len(txt)
        M = len(pat)
        indexes = []
        
        if M == 0:
            return ''
            
        # Create LPS
        lps = [0] * M
        prevLPS, i = 0, 1
        
        while i < M:
            if pat[i] == pat[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        # search
        i, j = 0, 0
        while i < N:
            if txt[i] == pat[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == M:
                indexes.append(i - M + 1)
                j = lps[j - 1]
                
        return indexes if len(indexes) != 0 else ''
