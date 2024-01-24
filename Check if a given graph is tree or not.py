'''
You are given an undirected graph of N nodes and M edges. Return 1 if the graph is a tree, else return 0.

Note: The input graph can have self-loops and multiple edges.
'''


from collections import defaultdict


class Solution:
    def isTree(self, n, m, edges):
        
        graph = defaultdict(list)
        
        for pair in edges:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
            
        visited = set()
        
        def dfs(s, prev):
            if s in visited:
                return False
            
            visited.add(s)
            for neighbor in graph[s]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, s):
                    return False
            
            return True 
            
        return int(dfs(0, -1) and len(visited) == n)
