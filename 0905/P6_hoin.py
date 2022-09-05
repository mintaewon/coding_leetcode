class Solution:
    def maxProfit(self, prices):
        buy=prices[0]
        max_profit=0
        for i in range(len(prices)):
            curr = prices[i]
            if buy >= curr:
                buy=curr
            profit = curr - buy
            if profit>=max_profit:
                max_profit=profit
            else:
                pass
        
        return max_profit
                

solver = Solution()
prices = [7,1,5,3,6,4]
print(solver.maxProfit(prices))
