class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        best_profit = 0

        for p in prices[1:]:
            profit = p - min_price
            best_profit = max(best_profit, profit)
            min_price = min(min_price, p)

        return best_profit        