class Solution:
    def countCommas(self, n):
        total = 0
        start = 1000
        commas = 1

        while start <= n:
            end = start * 1000 - 1
            total += (min(n, end) - start + 1) * commas

            start *= 1000
            commas += 1

        return total