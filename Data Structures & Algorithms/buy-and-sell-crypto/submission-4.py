class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        l = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxP = max(maxP, profit)
            if prices[l] > prices[r]:
                l = r
            
        return maxP