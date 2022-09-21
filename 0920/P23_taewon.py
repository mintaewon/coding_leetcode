'''
이진탐색 문제
'''




class Solution:
    def findMin(self, nums: List[int]) -> int:
        answer = 99999
        
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)//2
            
            if nums[mid] > nums[end]:
                answer = min(answer, nums[end])
                start = mid+1
            else:
                answer = min(answer, nums[mid])
                end = mid-1
                
        return answer