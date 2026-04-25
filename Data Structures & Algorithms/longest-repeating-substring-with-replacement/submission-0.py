class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = defaultdict(int)
        res = 0
        l = 0
        max_frequency = 0

        for r in range(len(s)):
            table[s[r]] += 1
            max_frequency = max(max_frequency, table[s[r]])
            if (r - l + 1) - max_frequency > k:
                table[s[l]] -= 1
                l += 1

        return r - l + 1
            