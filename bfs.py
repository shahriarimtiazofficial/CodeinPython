from collections import deque

graph = {
    'A': ['B', 'D'],
    'B': ['F', 'C'],
    'C': ['E', 'G'],
    'D': ['F'],
    'E': ['B', 'F'],
    'F': ['A'],
    'G': ['E']
}

def bfs(graph, start, target):

    queue = deque([[start]])  
    
    while queue:
        print("BFS Queue:", list(queue))
        path = queue.popleft()
        
    
        node = path[-1]
        if node == target:
            return path
        for neighbor in graph[node]:
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append(new_path)
    
    return 0 

shortest_path = bfs(graph, 'F', 'G')

print("Shortest Path:", shortest_path)
