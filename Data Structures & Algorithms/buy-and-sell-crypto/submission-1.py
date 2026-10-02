class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        min_price = prices[0]

        for sell in prices:
            max_diff = max(max_diff, sell - min_price)
            min_price = min(min_price, sell)

        return max_diff