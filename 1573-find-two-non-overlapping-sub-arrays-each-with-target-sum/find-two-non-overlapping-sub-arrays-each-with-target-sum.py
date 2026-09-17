class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        best = [float('inf')] * n
        prefix_index = {0: -1}

        prefix_sum = 0
        min_len = float('inf')
        answer = float('inf')

        for i in range(n):
            prefix_sum += arr[i]

            required = prefix_sum - target

            if required in prefix_index:
                start = prefix_index[required] + 1
                current_len = i - prefix_index[required]

                if start > 0 and best[start - 1] != float('inf'):
                    answer = min(
                        answer,
                        current_len + best[start - 1]
                    )

                min_len = min(min_len, current_len)

            best[i] = min_len
            prefix_index[prefix_sum] = i

        if answer == float('inf'):
            return -1

        return answer