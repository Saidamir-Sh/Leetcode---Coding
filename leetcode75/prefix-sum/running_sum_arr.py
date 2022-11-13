# 1
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = nums[0]
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] + nums[i]
        return ans

# 2
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
             nums[i] += nums[i-1]
        return nums