class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currProfit, bestProfit = 0, 0
        b = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < b:
                b = prices[i]
            elif prices[i] > b:
                currProfit = prices[i] - b
                bestProfit = max(currProfit, bestProfit)

        return bestProfit