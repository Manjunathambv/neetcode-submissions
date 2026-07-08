class Solution:
    def maxProfit(self, prices: List[int]) -> int:

# 0, 1, 2, 3, 4, 5
# 10, 1, 5, 6, 7,1
        min_value = prices[0]
        max_value = 0
        for value in range(len(prices)):
            min_value = min(min_value, prices[value])
            profit = prices[value] - min_value
            max_value = max(max_value, profit)
        return max_value