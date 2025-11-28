class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        self.components_count = 0
        def dfs(current_node, parent_node):
            current_sum = values[current_node]
            for neighbor in graph[current_node]:
                if neighbor != parent_node:
                    child_remainder = dfs(neighbor, current_node)
                    
                    current_sum += child_remainder
            if current_sum % k == 0:
                self.components_count += 1
                return 0 
            else:
                return current_sum
        dfs(0, -1)
        
        return self.components_count
    
print(Solution().maxKDivisibleComponents(n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3))