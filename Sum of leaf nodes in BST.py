'''
Given a Binary Search Tree with n nodes, find the sum of all leaf nodes. BST has the following property (duplicate nodes are possible):

    The left subtree of a node contains only nodes with keys less than the node’s key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node’s key.

Your task is to determine the total sum of the values of the leaf nodes.

Note: Input array arr doesn't represent the actual BST, it represents the order in which the elements will be added into the BST.
'''


class Solution:
    def sumOfLeafNodes(self, root):
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return
            if not root.left and not root.right:
                ans += root.data
                return
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return ans
