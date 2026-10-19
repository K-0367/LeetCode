class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        lenn = len(nums)
        l, r = 0, lenn - 1
        ans = []
        ans_set = set()
        if nums[l] == nums[r] and nums[l] == target:
            return list(range(0, lenn))
        while l <= r:
            mid = (l + r) // 2
            print(nums[l], nums[r], nums[mid])
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                ans_set.add(mid)
                # if nums[r] == target:
                #     ans_set.add(r)
                # if nums[l] == target:
                #     ans_set.add(l)
                r = mid - 1


        l, r = 0, lenn - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                ans_set.add(mid)
                l = mid + 1
                # r = mid - 1
        ans = sorted(list(ans_set))
        print(ans)
        if len(ans) <= 1:
            return ans
        return list(range(ans[0], ans[-1] + 1))