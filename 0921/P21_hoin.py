class Solution:
    def maxSubArray(self, nums):
        curr_sum = 0
        curr_max = -99999
        for i in range(len(nums)):
            curr_sum = max(curr_sum, 0) + nums[i]
            curr_max = max(curr_sum, curr_max)
            
        return curr_max
