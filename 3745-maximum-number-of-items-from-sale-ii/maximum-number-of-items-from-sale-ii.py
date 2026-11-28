from collections import defaultdict
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        cheapest = min(price for _, price in items)
        max_factor = max(factor for factor, _ in items)

        # Count how many items have each factor
        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1

        # mult_count[x] = total items whose factor is a multiple of x (including x itself)
        mult_count = freq[:]
        for x in range(1, max_factor + 1):
            if freq[x] > 0:
                for m in range(2 * x, max_factor + 1, x):
                    mult_count[x] += freq[m]

        # Group profitable 2-item deals (price < 2 * cheapest) by their price
        deals = defaultdict(int)
        for factor, price in items:
            free_choices = mult_count[factor] - 1  # exclude the item itself (i != j)
            if free_choices > 0 and price < 2 * cheapest:
                deals[price] += free_choices

        total_items = 0
        for price in sorted(deals):
            can_buy = min(deals[price], budget // price)
            total_items += 2 * can_buy
            budget -= can_buy * price

        # Spend remaining budget on the single cheapest item
        total_items += budget // cheapest
        return total_items
