
from math import inf
import heapq
# The following two exampls are from the Grokking algorithm book


class ABFinish_triangle:
    graph: dict
    costs: dict
    parents: dict

    def __init__(self):
        self.graph = {}
        self.graph["start"] = {}
        self.graph["start"]["a"] = 6
        self.graph["start"]["b"] = 2

        self.graph["a"] = {}
        self.graph["a"]["fin"] = 1

        self.graph["b"] = {}
        self.graph["b"]["a"] = 3
        self.graph["b"]["fin"] = 5

        self.graph["fin"] = {}

        # the costs table
        infinity = float("inf")
        self.costs = {}
        self.costs["a"] = 6
        self.costs["b"] = 2
        self.costs["fin"] = infinity

        # the parents table
        self.parents = {}
        self.parents["a"] = "start"
        self.parents["b"] = "start"
        self.parents["fin"] = None


class PianoTrade:
    graph: dict
    costs: dict
    parents: dict

    def __init__(self):
        self.graph = {}
        self.graph['Books'] = {}
        self.graph['Books']['LP'] = 5
        self.graph["Books"]['Poster'] = 0

        self.graph['LP'] = {}
        self.graph['LP']['Drum'] = 20
        self.graph['LP']['Guitar'] = 15

        self.graph['Poster'] = {}
        self.graph['Poster']['Guitar'] = 30
        self.graph['Poster']['Drum'] = 35

        self.graph['Guitar'] = {}
        self.graph['Guitar']['Piano'] = 20

        self.graph['Drum'] = {}
        self.graph['Drum']['Piano'] = 10

        self.graph['Piano'] = {}

        # define costs
        self.costs = {}
        self.costs['LP'] = 5
        self.costs['Poster'] = 0
        self.costs['Guitar'] = inf
        self.costs['Drum'] = inf
        self.costs['Piano'] = inf

        # the parents table
        self.parents = {}
        self.parents['LP'] = 'Books'
        self.parents['Poster'] = 'Books'
        self.parents['Guitar'] = None
        self.parents['Drum'] = None
        self.parents['Piano'] = None


def least_cost_node(costs: dict, processed: set):
    lowest_cost = inf
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra_algo(graph: dict, costs: dict, parents: dict):

    processed = set()

    node = least_cost_node(costs, processed)

    while node is not None:
        current_cost = costs[node]
        neighbours = graph[node]

        for n in neighbours.keys():
            print(f"looking at neighbour {n}")
            new_cost = current_cost + neighbours[n]

            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node

        processed.add(node)
        node = least_cost_node(costs, processed)

    print("Cost from the start to each node:")
    print(costs)


# A-B-Finish triangle example in the book
# print(dijkstra_algo(ABFinish_triangle().graph,
#       ABFinish_triangle().costs, ABFinish_triangle().parents))

# Piano-trade example in the book

print(dijkstra_algo(PianoTrade().graph, PianoTrade().costs, PianoTrade().parents))


#  TODO: replace the least cost node function with Heap
def dijkstra_algo_with_min_heap(graph: dict, costs: dict, parents: dict):
    processed = set()
    min_heap = []
    for key, value in costs.items():
        if value != inf:
            heapq.heappush(min_heap, (key, value))

    while len(min_heap) != 0:
        current_node, current_cost = heapq.heappop(min_heap)

        neighbours = graph[current_node]

        if current_node in processed:
            continue

        for n in neighbours:
            new_cost = current_cost + neighbours[n]

            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = current_node
                heapq.heappush(min_heap, (n, new_cost))

    return costs, parents


print(dijkstra_algo_with_min_heap(PianoTrade().graph,
      PianoTrade().costs, PianoTrade().parents))
