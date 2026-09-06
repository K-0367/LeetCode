class Solution:
    def minPrice(self, prices, discounts):
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        total = 0.0

        n = min(len(prices), len(discounts))

        for i in range(n):
            total += prices[i] * (100 - discounts[i]) / 100.0

        for i in range(n, len(prices)):
            total += prices[i]

        return total