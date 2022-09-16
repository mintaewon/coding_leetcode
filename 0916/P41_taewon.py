class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        cnt = 1
        answer = -9999
        sort_nums = sorted(set(nums))

        for i in range(len(sort_nums)-1):
            if sort_nums[i+1]-sort_nums[i] == 1:
                cnt+=1
            else:
                answer = max(answer, cnt)
                cnt=1
                
        answer = max(answer, cnt)
        return answer