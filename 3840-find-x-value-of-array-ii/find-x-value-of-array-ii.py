class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # tree[node][r] = number of prefixes
        # having product % k == r
        tree = [[0] * k for _ in range(4 * n)]

        # product of entire segment
        prod = [1] * (4 * n)

        def build(node, l, r):
            if l == r:
                v = nums[l] % k
                prod[node] = v
                tree[node][v] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node)

        def merge(node):
            left = node * 2
            right = node * 2 + 1

            prod[node] = (prod[left] * prod[right]) % k

            # Prefixes completely inside left
            for x in range(k):
                tree[node][x] = tree[left][x]

            # Prefixes that use left + some prefix of right
            for x in range(k):
                new_rem = (prod[left] * x) % k
                tree[node][new_rem] += tree[right][x]

        def update(node, l, r, pos, value):
            if l == r:
                v = value % k
                prod[node] = v

                for x in range(k):
                    tree[node][x] = 0

                tree[node][v] = 1
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(node * 2, l, mid, pos, value)
            else:
                update(node * 2 + 1, mid + 1, r, pos, value)

            merge(node)

        # Returns (product, counts)
        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return prod[node], tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left_prod, left_count = query(
                node * 2, l, mid, ql, qr
            )

            right_prod, right_count = query(
                node * 2 + 1, mid + 1, r, ql, qr
            )

            result_count = left_count[:]

            for x in range(k):
                new_rem = (left_prod * x) % k
                result_count[new_rem] += right_count[x]

            result_prod = (left_prod * right_prod) % k

            return result_prod, result_count

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:

            # Permanent update
            update(1, 0, n - 1, index, value)

            # Query nums[start ... n-1]
            _, counts = query(
                1, 0, n - 1,
                start,
                n - 1
            )

            ans.append(counts[x])

        return ans