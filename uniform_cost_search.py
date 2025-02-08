graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

def find_min_cost(queue):
    min_index = 0
    for i in range(len(queue)):
        if queue[i][0] < queue[min_index][0]:
            min_index = i
    return min_index

def uniform_cost_search(graph, start, goal):
    queue = [(0, [start])]
    visited = set()

    while queue:
        min_index = find_min_cost(queue)
        cost, path = queue.pop(min_index)
        current_node = path[-1]

        if current_node in visited:
            continue

        visited.add(current_node)
        if current_node == goal:
            return cost, path

        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in visited:
                new_cost = cost + weight
                new_path = path + [neighbor]
                queue.append((new_cost, new_path))

    return float('inf'), []

cost, path = uniform_cost_search(graph, 'A', 'D')
print(f"Shortest path: {path}")
print(f"Total cost: {cost}")
