'''
Given a binary tree with n nodes and a non-negative integer k, the task is to count the number of special nodes.
A node is considered special if there exists at least one leaf in its subtree such that the distance between the node and leaf is exactly k.

Note: Any such node should be counted only once. For example, if a node is at a distance k from 2 or more leaf nodes, then it would add only 1 to our count.
'''


from collections import deque
class Solution:
    #Function to return count of nodes at a given distance from leaf nodes.
    def printKDistantfromLeaf(self, root, k):
        queue = deque([(root, [], 0)])
        leaf_paths = []
        while queue:
            node, path, distance = queue.popleft()
            
            if not node.left and not node.right:
                leaf_paths.append((path + [node], distance + 1))
                continue
            
            if node.left:
                queue.append((node.left, path + [node], distance + 1))
                
            if node.right:
                queue.append((node.right, path + [node], distance + 1))
            
        return len(set([path[-k - 1] for path, distance in leaf_paths if distance - 1 >= k]))
