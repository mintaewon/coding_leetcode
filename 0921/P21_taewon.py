'''
투포인터로 접근했다가 실패함
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_num = 0
        answer = -999999999999999
        
        for i in range(len(nums)):
            sum_num += nums[i]
            answer = max(answer, sum_num)
            
            if sum_num < 0:
                sum_num = 0
        return answer