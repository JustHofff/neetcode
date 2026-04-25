class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        ss1 = sorted(s1)

        for r in range(len(s1), len(s2) + 1):
            if ss1 == sorted(s2[l:r]):
                return True
            l += 1
        
        return False