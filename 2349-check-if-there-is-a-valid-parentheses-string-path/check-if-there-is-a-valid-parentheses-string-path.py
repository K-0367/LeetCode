class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Path length must be even for a valid parentheses string
        if (m + n - 1) % 2 != 0:
            return False

        # dp[i][j] = set of possible balances at (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        # Starting cell must be '('
        if grid[0][0] == ')':
            return False

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                for balance in range(m + n):
                    new_balance = balance

                    if grid[i][j] == '(':
                        new_balance += 1
                    else:
                        new_balance -= 1

                    # Balance can never become negative
                    if new_balance < 0:
                        continue

                    # From top
                    if i > 0 and balance in dp[i - 1][j]:
                        dp[i][j].add(new_balance)

                    # From left
                    if j > 0 and balance in dp[i][j - 1]:
                        dp[i][j].add(new_balance)

        # Valid parentheses string must finish with balance 0
        return 0 in dp[m - 1][n - 1]