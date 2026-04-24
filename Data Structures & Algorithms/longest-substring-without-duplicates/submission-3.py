class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        best = 0
        l = 0

        for i in range(len(s)):
            if s[i] in m:
                l = max(m[s[i]] + 1, l)
            m[s[i]] = i
            best = max(i - l + 1, best)
    
        return best