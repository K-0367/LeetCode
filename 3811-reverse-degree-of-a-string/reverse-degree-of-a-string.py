class Solution:
    def reverseDegree(self, s):
        total = 0

        for i in range(len(s)):
            value = ord('z') - ord(s[i]) + 1
            position = i + 1
            total += value * position

        return total