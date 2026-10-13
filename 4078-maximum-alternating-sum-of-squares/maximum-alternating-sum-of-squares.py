class Solution:
    def maxAlternatingSum(self, nums):
        nums = sorted(x * x for x in nums)
        k = (len(nums) + 1) // 2

        return sum(nums[-k:]) - sum(nums[:-k])