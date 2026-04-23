class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        best = 0

        for c in s:
            if c in substring:
                while substring:
                    p = substring.pop(0)
                    if p == c:
                        break
            substring.append(c)
            best = max(len(substring), best)
    
        return best