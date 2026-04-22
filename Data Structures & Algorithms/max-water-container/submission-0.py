class Solution:
    def maxArea(self, heights: List[int]) -> int:
        cA, mA = 0, 0
        l, r = 0, len(heights) - 1
        while l < r:
            small = min(heights[l], heights[r])
            cA = (r - l) * small
            mA = max(cA, mA)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return mA

