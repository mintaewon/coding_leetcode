class Solution:
    def longestConsecutive(self, nums):
        if len(nums)==0:
            return 0
        nums = sorted(list(set(nums)))
        count = 0
        max_count=0
        for i in range(len(nums)-1):
            gap = nums[i+1]- nums[i]
            
            if gap==1:
                count+=1
                max_count = max(max_count, count)
            else :
                count=0
        return max_count+1
