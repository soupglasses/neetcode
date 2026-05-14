class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent_idx = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(node):
            if parent_idx[node] != node:
                return find(parent_idx[node])
            else:
                return node

        def union(left, right):
            left, right = find(left), find(right)
            if left == right:
                return 0
            if rank[right] > rank[left]:
                rank[right] += rank[left]
                parent_idx[left] = right
            else:
                rank[left] += rank[right]
                parent_idx[right] = left
            return 1

        result = n
        for left, right in edges:
            result -= union(left, right)
        return result