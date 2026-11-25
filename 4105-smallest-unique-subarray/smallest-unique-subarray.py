from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # Double rolling hash parameters to prevent collisions
        MOD1, MOD2 = 1_000_000_007, 1_000_000_009
        BASE1, BASE2 = 131_542_391, 265_443_576

        # Offset values in case nums contains negative numbers or zeros
        min_val = min(nums)
        arr = [x - min_val + 1 for x in nums]

        # Precompute prefix hashes and powers
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)

        for i in range(n):
            h1[i + 1] = (h1[i] * BASE1 + arr[i]) % MOD1
            h2[i + 1] = (h2[i] * BASE2 + arr[i]) % MOD2
            p1[i + 1] = (p1[i] * BASE1) % MOD1
            p2[i + 1] = (p2[i] * BASE2) % MOD2

        def has_unique_of_length(k: int) -> bool:
            seen = set()
            duplicates = set()
            pk1, pk2 = p1[k], p2[k]

            for i in range(n - k + 1):
                sub_h1 = (h1[i + k] - h1[i] * pk1) % MOD1
                sub_h2 = (h2[i + k] - h2[i] * pk2) % MOD2
                # Pack two 32-bit hashes into a single integer key to save memory
                key = (sub_h1 << 32) | sub_h2

                if key in seen:
                    duplicates.add(key)
                else:
                    seen.add(key)

            return len(seen) > len(duplicates)

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique_of_length(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
