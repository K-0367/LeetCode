class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        out_of_order = []
        for i in range(n):
            if nums[i] != i:
                out_of_order.append(i)

        if not out_of_order:
            return 0

        prev = out_of_order[0]
        for i in range(1, len(out_of_order)):
            prev = out_of_order[i] & prev
            
        return prev
