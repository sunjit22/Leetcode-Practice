class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s, key=lambda x:ord(x)) ==  sorted(t, key=lambda x:ord(x))
        