class Solution:
    def countSpecialIntegers(self, nums):
        positions = {}

        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

        count = 0

        for num in positions:
            indices = positions[num]

            if len(indices) == 3:
                i1, i2, i3 = indices

                if i2 - i1 == i3 - i2:
                    count += 1

        return count