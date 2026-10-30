import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        pq = [(0, 0, 1)]
        dist = {(0, 1): 0}

        while pq:
            cost, u, count = heapq.heappop(pq)

            if cost != dist.get((u, count), float('inf')):
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:
                if labels[v] == labels[u]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + w
                state = (v, new_count)

                if new_cost < dist.get(state, float('inf')):
                    dist[state] = new_cost
                    heapq.heappush(pq, (new_cost, v, new_count))

        return -1