''''

투포인터로 접근했으나 시간초과 간당간당함

밑에 O(n^2) 보다 빠른 방법을 사용해야된다고 나와있음

이중 for문을 줄이기 위해 target에서 빼준 값을 저장 후 공백으로 만들어 in 연산

'''

# 투포인터 - 시간초과
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for start in range(len(nums)-1):
            end=start+1
            while end<len(nums):
                if nums[start]+nums[end] == target:
                    return [start, end]
                end+=1


# 최종
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target-nums[i]
            nums[i] = None
            if temp in nums:
                return [i, nums.index(temp)]
