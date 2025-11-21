class Solution:
    def countPalindromicSubsequence(s: str) -> int:
        if len(s) <= 2:
            return 0

        chars = set(s)
        res = 0
        for ch in chars:
            first = s.find(ch)
            last = s.rfind(ch)

            if first != last:
                res += len(set(s[first + 1:last]))

        return res
    
    
print(Solution.countPalindromicSubsequence("bbcbaba"))
print(Solution.countPalindromicSubsequence("abcdabcdabcd"))