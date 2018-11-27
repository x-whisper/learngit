graph = {'start': {'a': 6, 'b': 2}, 'a': {'fin': 1}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}
infinity = float('inf')
costs = {'a': 6, 'b': 2, 'fin': infinity}
parents = {'a': 'start', 'b': 'start', 'fin': None}
proccessed = []

def find_lowest_cost_node(costs):
    lowest_cost_node = None
    lowest_cost = float('inf')
    for node in costs.keys():
        try:
            if node not in proccessed and costs[node] < lowest_cost:
                lowest_cost = costs[node]
                lowest_cost_node = node
        except:
            print("something wrong")
            print(costs[node], lowest_cost)
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for neighbor in neighbors.keys():
        new_cost = cost + neighbors[neighbor]
        if costs[neighbor] > new_cost:
            costs[neighbor] = new_cost
            parents[neighbor] = node
    proccessed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
print(parents)