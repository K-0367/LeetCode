
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        target = max(nums)
        moves = 0

        for num in nums:
            moves += target - num

        return moves
