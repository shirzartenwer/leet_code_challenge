import heapq
from math import inf
from typing import List
import time


class DijkstraSolution:
    def dijkstra_algo_with_min_heap(self, graph: dict, costs: dict, stops: dict, src: int, target_node: int, k: int):
        min_heap = []

        # always remember to handle the edge case
        if src not in graph.keys() or target_node not in graph.keys():
            return -1

        costs[src] = 0
        stops[src] = -1

        # how python handle the tuple comparison is by digit
        # so when the cost is the same, we want heap to compare number of stops
        # that's why it's structured as (cost, stops, node)
        heapq.heappush(min_heap, (0, -1, src))

        while len(min_heap) != 0:
            current_cost, current_stops, current_node = heapq.heappop(min_heap)

            neighbours = graph[current_node]
            if current_node == target_node:
                # It doesn't have to use all k stops. The condition was at most k stops
                if current_stops <= k:
                    return current_cost
                else:
                    continue
            # This will just make if faster by skipping the cases that will add cases that
            # won't fit into condition anyway
            if current_stops == k:
                continue

            for n in neighbours:
                new_cost = current_cost + neighbours[n]
                new_stops = current_stops + 1

                if costs[n] > new_cost or stops[n] > new_stops:
                    costs[n] = new_cost
                    stops[n] = new_stops
                    heapq.heappush(min_heap, (new_cost, new_stops, n))

        return -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for ele in flights:
            if ele[0] not in graph.keys():
                graph[ele[0]] = {}
            graph[ele[0]][ele[1]] = ele[2]
            if ele[1] not in graph.keys():
                graph[ele[1]] = {}

        costs = {}
        for key in graph.keys():
            costs[key] = inf

        stops = {}

        for key in graph.keys():
            stops[key] = inf

        return self.dijkstra_algo_with_min_heap(graph, costs, stops, src, dst, k)


class BackTrackingSolutionFromLeetCode:

    class Solution:
        def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

            # src -> (dst, cost)
            graph = {}
            for edge in flights:
                graph[edge[0]] = graph.get(edge[0], [])
                graph[edge[0]].append((edge[1], edge[2]))

            # find cheapest flight between src and dst
            #  @cache
            def helper(src, dst, k):
                # print(src, dst, k)
                if k < 0:
                    return inf

                ans = inf
                for neighbor in graph.get(src, []):
                    # cheapest flight between neighbor and dst + cost of src and neighbor
                    if neighbor[0] == dst:
                        ans = min(ans, neighbor[1])
                    else:
                        ans = min(ans, helper(
                            neighbor[0], dst, k - 1) + neighbor[1])

                return ans

            result = helper(src, dst, k)
            return -1 if result == inf else result


#  Testc case
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1

start_time_1 = time.time()
print(DijkstraSolution().findCheapestPrice(n, flights, 0, 3, 1))
end_time_1 = time.time()

start_time_2 = time.time()
print(BackTrackingSolutionFromLeetCode().Solution(
).findCheapestPrice(n, flights, 0, 3, 1))
end_time_2 = time.time()

print(
    f"The dijkstra took {end_time_1 - start_time_1}, the backtracking took {end_time_2 - end_time_1}")
