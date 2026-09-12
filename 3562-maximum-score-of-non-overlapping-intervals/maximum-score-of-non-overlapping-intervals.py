from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Sort by right endpoint
        arr = sorted(
            (r, l, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        ends = [x[0] for x in arr]

        # dp[i][k] = best answer using first i intervals
        # and choosing at most k intervals
        dp = [[(0, []) for _ in range(5)]
              for _ in range(n + 1)]

        for i in range(1, n + 1):
            r, l, w, idx = arr[i - 1]

            # Find intervals ending strictly before l
            prev = bisect_left(ends, l, 0, i - 1)

            for k in range(1, 5):
                # Option 1: Skip current interval
                skip_score, skip_ids = dp[i - 1][k]

                # Option 2: Take current interval
                take_score, take_ids = dp[prev][k - 1]

                take_score += w
                take_ids = take_ids + [idx]
                take_ids.sort()

                # Choose maximum score
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_ids)

                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_ids)

                # Same score: lexicographically smaller indices
                else:
                    dp[i][k] = min(
                        (take_score, take_ids),
                        (skip_score, skip_ids)
                    )

        return dp[n][4][1]