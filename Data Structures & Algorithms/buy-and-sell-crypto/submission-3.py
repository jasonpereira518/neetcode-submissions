class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minimum = prices[0]

        for sell in prices:
            maxP = max(maxP, sell-minimum)
            minimum = min(sell, minimum)

        return maxP
