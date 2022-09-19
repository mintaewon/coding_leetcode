class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        
        # 오른쪽으로 곱
        temp = 1
        for i in range(len(nums)):
            answer.append(temp)
            temp *= nums[i]
            
        # 왼쪽으로 곱
        temp = 1
        for j in range(len(nums)-1,-1,-1):
            answer[j] *= temp
            temp *= nums[j]
                
        return answer