class Solution:
    def countSpecialIntegers(self, nums):
        positions = {}

        # Store indices of each number
        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

        count = 0

        # Check every distinct number
        for num in positions:
            indices = positions[num]

            # At least 3 occurrences
            if len(indices) >= 3:
                d = indices[1] - indices[0]
                special = True

                # Check all consecutive gaps
                for i in range(2, len(indices)):
                    if indices[i] - indices[i - 1] != d:
                        special = False
                        break

                if special:
                    count += 1

        return count