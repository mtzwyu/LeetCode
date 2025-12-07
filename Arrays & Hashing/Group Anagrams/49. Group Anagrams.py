import collections
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            stortedS = ''.join(sorted(s))
            res[stortedS].append(s)
        return list(res.values())
        


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))