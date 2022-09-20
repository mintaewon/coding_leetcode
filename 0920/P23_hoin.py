
nums = [4,5,6,7,0,1,2]
N = len(nums)
min_num = nums[0]
for i in nums:
    min_num = min(i,min_num)
print(min_num)