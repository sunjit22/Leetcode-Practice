class Solution:
    def maxPower(self, s: str) -> int:
        maximum = 1
        curr = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                curr += 1
                maximum = max(maximum,curr)
            else:
                curr = 1
                maximum = max(maximum,curr)
        return maximum         