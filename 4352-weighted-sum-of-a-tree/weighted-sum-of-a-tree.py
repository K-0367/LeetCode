class Solution:
    def weightedSum(self, parent, nums):
        n = len(parent)

        # Build tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Find depth of each node and tree height
        depth = [0] * n
        depth[0] = 1

        stack = [0]
        height = 1

        while stack:
            node = stack.pop()

            height = max(height, depth[node])

            for child in children[node]:
                depth[child] = depth[node] + 1
                stack.append(child)

        # Calculate weighted sum
        total = 0

        for i in range(n):
            total += nums[i] * (height - depth[i] + 1)

        return total