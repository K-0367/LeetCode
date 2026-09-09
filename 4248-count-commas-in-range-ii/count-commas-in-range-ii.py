class Solution:
    def countCommas(self, n):
        count = 0
        place = 1000

        while place <= n:
            count += n - place + 1
            place *= 1000

        return count