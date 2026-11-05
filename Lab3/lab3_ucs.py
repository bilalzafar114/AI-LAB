import heapq
from collections import deque

WEIGHTED_GRAPH = {
    "A": [("B", 1), ("C", 2)],
    "B": [("D", 1), ("E", 1)],
    "C": [("F", 1), ("G", 10)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": [],
}

def ucs(graph, start, goal):
    pq = [(0, start, [start])]
    visited = set()
    processing_order = []
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        
        if node in visited:
            continue
        
        processing_order.append(node)
        visited.add(node)
        
        if node == goal:
            return path, cost, processing_order
            
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
                
    return None, float('inf'), processing_order

def bfs_weighted(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        node, path = queue.popleft()
        
        if node == goal:
            total_cost = 0
            for i in range(len(path) - 1):
                u, v = path[i], path[i+1]
                for neighbor, weight in graph[u]:
                    if neighbor == v:
                        total_cost += weight
                        break
            return path, total_cost
            
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return None, float('inf')


ucs_path, ucs_cost, ucs_order = ucs(WEIGHTED_GRAPH, "A", "G")

bfs_path, bfs_cost = bfs_weighted(WEIGHTED_GRAPH, "A", "G")

print("=== UCS RESULT ===")
print(f"Path: {ucs_path}")
print(f"Total Cost: {ucs_cost}")
print(f"Processing/Expansion Order: {ucs_order}")

print("\n=== BFS RESULT ===")
print(f"Path: {bfs_path}")
print(f"Total Cost (calculated independently): {bfs_cost}")