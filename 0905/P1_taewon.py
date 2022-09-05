''''

이중 for문 접근했으나

밑에 O(n^2) 보다 빠른 방법을 고려할 수 있다고함

'''

# 이중 for문
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]


# target에서 빼준 값을 저장 후 공백으로 만들어 in 연산
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target-nums[i]
            nums[i] = None
            if temp in nums:
                return [i, nums.index(temp)]
