class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = "".join(c.lower() for c in s if c.isalnum())
        start = 0
        end = len(formatted) - 1
        while start < end:
            if formatted[start] != formatted[end]:
                return False
            start += 1
            end -= 1
        return True