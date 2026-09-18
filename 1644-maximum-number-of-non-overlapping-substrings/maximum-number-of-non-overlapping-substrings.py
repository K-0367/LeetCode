class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        # First and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        # Find the smallest valid interval starting from position l
        def get_interval(l):
            r = last[ord(s[l]) - ord('a')]
            i = l

            while i <= r:
                x = ord(s[i]) - ord('a')

                # This character appeared before l,
                # so this interval cannot be valid.
                if first[x] < l:
                    return None

                r = max(r, last[x])
                i += 1

            return (l, r)

        intervals = []

        # Generate candidate intervals
        for i in range(n):
            if i == first[ord(s[i]) - ord('a')]:
                interval = get_interval(i)

                if interval is not None:
                    intervals.append(interval)

        # Choose maximum number of non-overlapping intervals.
        # Among equal counts, choosing the shortest intervals
        # gives the minimum total length.
        intervals.sort(key=lambda x: (x[1], x[1] - x[0] + 1))

        answer = []
        end = -1

        for l, r in intervals:
            if l > end:
                answer.append(s[l:r + 1])
                end = r

        return answer