class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, node) -> int:
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, left, right) -> bool:
        left, right = self.find(left), self.find(right)
        if left == right:
            return False
        if self.rank[right] > self.rank[left]:
            self.parent[left] = right
            self.rank[right] += self.rank[left]
        else:
            self.parent[right] = left
            self.rank[left] += self.rank[right]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu, result = DSU(n), n
        for left, right in edges:
            result -= dsu.union(left, right)
        return result