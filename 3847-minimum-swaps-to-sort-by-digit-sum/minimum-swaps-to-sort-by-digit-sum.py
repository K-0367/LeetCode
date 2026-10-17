class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))
        pos = {v: i for i, v in enumerate(arr)}
        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or pos[nums[i]] == i:
                continue

            cycle = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle += 1

            swaps += cycle - 1

        return swaps