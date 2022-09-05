class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = -99999
        minimum = 99999
        for i in range(len(prices)):
            minimum = min(prices[i], minimum)
            answer = max(answer, prices[i]-minimum)
        return answer