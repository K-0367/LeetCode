
from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            # Free servers whose requests have finished
            while busy and busy[0][0] <= time:
                end_time, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            # Find the first available server >= i % k
            server_id = available.bisect_left(i % k)

            # Wrap around if needed
            if server_id == len(available):
                server_id = 0

            server = available.pop(server_id)

            # Assign request
            count[server] += 1
            heapq.heappush(busy, (time + load[i], server))

        max_count = max(count)

        return [i for i in range(k) if count[i] == max_count]
