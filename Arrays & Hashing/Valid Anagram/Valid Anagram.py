class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        return s == t
        


print(Solution.isAnagram(Solution, "anagram", "nagaram"))  # True
print(Solution.isAnagram(Solution, "rat", "car"))  # False