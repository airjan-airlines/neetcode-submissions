class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # easiest idea: for each day, is there a later day with higher price?
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                temp_profit = prices[j] - prices[i]
                if temp_profit > profit:
                    profit = temp_profit
        
        #default is 0 anyway
        return profit