
import heapq

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        # Max heap for lower half, min heap for upper half
        low = []
        high = []

        delayed = {}

        low_size = high_size = 0
        low_sum = high_sum = 0

        def prune(heap, is_low):
            while heap:
                val = -heap[0] if is_low else heap[0]

                if delayed.get(val, 0) > 0:
                    delayed[val] -= 1
                    if delayed[val] == 0:
                        del delayed[val]

                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal low_size, high_size
            nonlocal low_sum, high_sum

            prune(low, True)
            prune(high, False)

            # Lower half should contain ceil(x / 2) elements
            while low_size > high_size + 1:
                prune(low, True)
                val = -heapq.heappop(low)

                heapq.heappush(high, val)

                low_size -= 1
                high_size += 1

                low_sum -= val
                high_sum += val

            while low_size < high_size:
                prune(high, False)
                val = heapq.heappop(high)

                heapq.heappush(low, -val)

                high_size -= 1
                low_size += 1

                high_sum -= val
                low_sum += val

            prune(low, True)
            prune(high, False)

        def add(val):
            nonlocal low_size, high_size
            nonlocal low_sum, high_sum

            prune(low, True)

            if not low or val <= -low[0]:
                heapq.heappush(low, -val)
                low_size += 1
                low_sum += val
            else:
                heapq.heappush(high, val)
                high_size += 1
                high_sum += val

            rebalance()

        def remove(val):
            nonlocal low_size, high_size
            nonlocal low_sum, high_sum

            prune(low, True)

            delayed[val] = delayed.get(val, 0) + 1

            if val <= -low[0]:
                low_size -= 1
                low_sum -= val

                if val == -low[0]:
                    prune(low, True)
            else:
                high_size -= 1
                high_sum -= val

                if high and val == high[0]:
                    prune(high, False)

            rebalance()

        def get_cost():
            prune(low, True)
            median = -low[0]

            return (
                median * low_size - low_sum
                + high_sum - median * high_size
            )

        # Cost of every window of size x
        costs = []

        for i in range(n):
            add(nums[i])

            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                costs.append(get_cost())

        # DP: minimum cost to select j non-overlapping windows
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    start = i - x

                    if prev[start] != INF:
                        curr[i] = min(
                            curr[i],
                            prev[start] + costs[start]
                        )

            prev = curr

        return prev[n]
