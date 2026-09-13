from bisect import bisect_left, bisect_right

class Solution:
    def distantSubarrays(self, nums, goal, k):
        n = len(nums)

        total = n * (n + 1) // 2

        # If k is 0, every subarray is distant
        if k == 0:
            return total

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        values = sorted(set(prefix))
        rank = {v: i + 1 for i, v in enumerate(values)}

        bit = [0] * (len(values) + 1)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            total = 0

            while i > 0:
                total += bit[i]
                i -= i & -i

            return total

        close = 0

        update(rank[0])

        for j in range(1, n + 1):
            current = prefix[j]

            low = current - goal - k
            high = current - goal + k

            left = bisect_right(values, low)
            right = bisect_left(values, high)

            close += query(right) - query(left)

            update(rank[current])

        return total - close