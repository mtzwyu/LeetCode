class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        def dfs(node, parent):
            cursum = values[node]
            for nei in adj_list[node]:
                if nei == parent: continue
                cursum += dfs(nei, node)
            if cursum % k==0:
                self.ans += 1
                return 0
            return cursum

        adj_list = [[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        print(adj_list)
        self.ans = 0
        dfs(0, -1)
        return self.ans
    
print(Solution().maxKDivisibleComponents(n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3))