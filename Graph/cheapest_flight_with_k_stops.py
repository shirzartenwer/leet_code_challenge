import heapq
from math import inf
from typing import List


class Solution:
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
