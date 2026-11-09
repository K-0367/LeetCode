import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        """
        1 <= k <= 105
        1 <= arrival.length, load.length <= 105
        arrival.length == load.length
        1 <= arrival[i], load[i] <= 109
        arrival is strictly increasing
        """

        counts: dict[int, int] = {}
        maxCount = 0
        generation = 0 
        usedHeap: list[tuple(int,int,int)] = [] # (nextAvailTime, serverGeneration, serverIndex)
        availHeap = [(1, i+1) for i in range(k)] # (serverGeneration, serverIndex)
        for i in range(len(arrival)):
            if i % k == 0: generation += 1
            t, w = arrival[i], load[i]
            while usedHeap and usedHeap[0][0] <= t:
                server = heapq.heappop(usedHeap)
                heapq.heappush(availHeap, (server[1], server[2]))
            if not availHeap: continue
            while availHeap[0] < (generation, ((i%k)+1)):
                server = heapq.heappop(availHeap)
                heapq.heappush(availHeap, (server[0] + 1, server[1]))
            server = heapq.heappop(availHeap)
            counts[server[1]] = counts.get(server[1], 0) + 1
            maxCount = max(maxCount, counts[server[1]])
            heapq.heappush(usedHeap, (t + w, generation, server[1]))
        return [server-1 for server in counts if counts[server] == maxCount]