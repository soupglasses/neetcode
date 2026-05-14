"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        
        queue = deque([node])
        seen = dict()
        seen[node] = Node(node.val)

        while queue:
            current = queue.popleft()
            for neigh in current.neighbors:
                if neigh not in seen:
                    seen[neigh] = Node(neigh.val)
                    queue.append(neigh)
                seen[current].neighbors.append(seen[neigh])

        return seen[node]
