class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        ancestors = {}

        def dfs(node):
            ch = s[node]

            # Save previous ancestor of this character
            old = ancestors.get(ch)

            if old is not None:
                new_parent[node] = old

            ancestors[ch] = node

            for child in children[node]:
                dfs(child)

            # Restore previous value
            if old is None:
                del ancestors[ch]
            else:
                ancestors[ch] = old

        dfs(0)

        # Construct modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        answer = [0] * n

        def calculate(node):
            size = 1

            for child in new_children[node]:
                size += calculate(child)

            answer[node] = size
            return size

        calculate(0)

        return answer