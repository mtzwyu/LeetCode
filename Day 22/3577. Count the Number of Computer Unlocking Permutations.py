import math
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
        
        return math.factorial(n-1) % (10**9 + 7)
    
    
    
print(Solution().countPermutations([38,223,100,123,406,234,256,93,222,259,233,69,139,245,45,98,214]))