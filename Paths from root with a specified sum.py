'''
Given a Binary tree and a sum S, print all the paths, starting from root, that sums upto the given sum. Path may not end on a leaf node.
'''


class Solution:
    def printPaths(self, root, sum):
        def solve(r, s, p):
            if r:
                p = p + [r.data]
                if r.data == s:
                    ans.append(p)
                solve(r.left, s - r.data, p)
                solve(r.right, s - r.data, p)
                
        ans = []
        solve(root, sum, [])
        return ans
