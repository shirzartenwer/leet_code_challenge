
from math import inf

# The following two exampls are from the Grokking algorithm book


def a_b_finish_triangle():
    # the graph
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5

    graph["fin"] = {}

    # the costs table
    infinity = float("inf")
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity

    # the parents table
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    processed = []

    def find_lowest_cost_node(costs, processed):
        lowest_cost = float("inf")
        lowest_cost_node = None
        # Go through each node.
        for node in costs:
            cost = costs[node]
            # If it's the lowest cost so far and hasn't been processed yet...
            if cost < lowest_cost and node not in processed:
                # ... set it as the new lowest-cost node.
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    # Find the lowest-cost node that you haven't processed yet.
    node = find_lowest_cost_node(costs, processed)
    # If you've processed all the nodes, this while loop is done.
    while node is not None:
        cost = costs[node]
        # Go through all the neighbors of this node.
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # If it's cheaper to get to this neighbor by going through this node...
            if costs[n] > new_cost:
                # ... update the cost for this node.
                costs[n] = new_cost
                # This node becomes the new parent for this neighbor.
                parents[n] = node
        # Mark the node as processed.
        processed.append(node)
        # Find the next node to process, and loop.
        node = find_lowest_cost_node(costs, processed)

    print("Cost from the start to each node:")
    print(costs)


def piano_trade():

    graph = {}
    graph['Books'] = {}
    graph['Books']['LP'] = 5
    graph["Books"]['Poster'] = 0

    graph['LP'] = {}
    graph['LP']['Drum'] = 20
    graph['LP']['Guitar'] = 15

    graph['Poster'] = {}
    graph['Poster']['Guitar'] = 30
    graph['Poster']['Drum'] = 35

    graph['Guitar'] = {}
    graph['Guitar']['Piano'] = 20

    graph['Drum'] = {}
    graph['Drum']['Piano'] = 10

    graph['Piano'] = {}

    # define costs
    costs = {}
    costs['LP'] = 5
    costs['Poster'] = 0
    costs['Guitar'] = inf
    costs['Drum'] = inf
    costs['Piano'] = inf

    # the parents table
    parents = {}
    parents['LP'] = 'Books'
    parents['Poster'] = 'Books'
    parents['Guitar'] = None
    parents['Drum'] = None
    parents['Piano'] = None

    processed = set()

    def least_cost_node(costs: dict, processed: set):
        lowest_cost = inf
        lowest_cost_node = None

        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

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


print(a_b_finish_triangle())
print(piano_trade())


#  TODO: replace the least cost node function with Heap
