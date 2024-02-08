'''
Given a binary tree with n nodes, determine whether all the leaf nodes are at the same level or not. 
Return true if all leaf nodes are at the same level, and false otherwise.
'''


class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        leaf_levels = set()
        
        def traverse(node, level):
            if not node:
                return
            if not node.left and not node.right:
                leaf_levels.add(level)
            traverse(node.left, level+1)
            traverse(node.right, level+1)
            
        traverse(root, 0)
        return len(leaf_levels) == 1
