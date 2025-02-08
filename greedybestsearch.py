graph = {
    'A': {'B': 32, 'C': 25, 'D': 35},
    'B': {'E': 19},
    'C': {'E': 19, 'F': 17},
    'D': {'F': 17},
    'E': {'H': 10},
    'F': {'G': 0},
    'G': {},
    'H': {'G': 0}
}

heuristic = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0,
    'H': 10
}

def greedy_best_first_search(start, goal):
    open_list = [start]
    closed_list = []
    parent_map = {start: None}

    while open_list:
        current = min(open_list, key=lambda node: heuristic[node])
        open_list.remove(current)
        closed_list.append(current)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent_map[current]
            return path[::-1]

        for neighbor in graph[current]:
            if neighbor not in closed_list and neighbor not in open_list:
                open_list.append(neighbor)
                parent_map[neighbor] = current

    return None

start_node = 'A'
goal_node = 'G'
result_path = greedy_best_first_search(start_node, goal_node)
print("Path from", start_node, "to", goal_node, ":", result_path)
