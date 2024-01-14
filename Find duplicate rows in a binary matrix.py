'''
Given a boolean matrix of size RxC where each cell contains either 0 or 1, 
find the row numbers (0-based) of row which already exists or are repeated.
'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.count = 0


class Solution:
    def repeatedRows(self, arr, m ,n):
        root = TrieNode()
        
        ans = []
        for i in range(m):
            curr = root
            for j in range(n):
                if not arr[i][j] in curr.children:
                    curr.children[arr[i][j]] = TrieNode()
                curr = curr.children[arr[i][j]]
            curr.count += 1
            if curr.count > 1:
                ans.append(i)
        return ans
