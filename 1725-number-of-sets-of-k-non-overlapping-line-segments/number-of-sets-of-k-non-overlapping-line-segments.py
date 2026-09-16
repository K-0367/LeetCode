class Solution:
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        # The answer is C(n + k - 1, 2 * k)

        N = n + k - 1

        fact = [1] * (N + 1)

        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (N + 1)

        inv_fact[N] = pow(fact[N], MOD - 2, MOD)

        for i in range(N - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        ans = fact[N]
        ans = ans * inv_fact[2 * k] % MOD
        ans = ans * inv_fact[N - 2 * k] % MOD

        return ans