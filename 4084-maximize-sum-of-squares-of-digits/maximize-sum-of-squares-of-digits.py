class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        result = []
        remaining = sum

        for _ in range(num):
            digit = min(9, remaining)
            result.append(str(digit))
            remaining -= digit

        if remaining != 0:
            return ""

        return "".join(result)