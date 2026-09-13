class Solution:
    def cyclicShift(self, n, grid, rowShift, colShift):

        # Step 1: Shift each row left
        for i in range(n):
            k = rowShift[i] % n
            grid[i] = grid[i][k:] + grid[i][:k]

        # Step 2: Shift each column upward
        for j in range(n):
            k = colShift[j] % n

            column = []

            for i in range(n):
                column.append(grid[i][j])

            column = column[k:] + column[:k]

            for i in range(n):
                grid[i][j] = column[i]

        return grid