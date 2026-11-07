import heapq


graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

f = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}

def perform_graph_search(topology, heuristic_map, origin, target):
    frontier = []
    heapq.heappush(frontier, (heuristic_map[origin], 0, origin, [origin]))
    
    node = []
    closed_set = set()
    
    while frontier:
        expected_total, current_depth, active_node, current_path = heapq.heappop(frontier)
        
        if active_node in closed_set:
            continue
        
        node.append(active_node)
        closed_set.add(active_node)
        
        if active_node == target:
            return current_path, current_depth, node, len(node)
            
        for successor, edge_weight in topology.get(active_node, []):
            if successor not in closed_set:
                cumulative_g = current_depth + edge_weight
                projected_f = cumulative_g + heuristic_map[successor]
                heapq.heappush(frontier, (projected_f, cumulative_g, successor, current_path + [successor]))
                
    return None, float('inf'), node, len(node)

null_heuristic = {key: 0 for key in f}
ucs_route, ucs_total_weight, ucs_nodes_log, ucs_total_expansions = perform_graph_search(
    graph, null_heuristic, "S", "G"
)
astar_route, astar_total_weight, astar_nodes_log, astar_total_expansions = perform_graph_search(
    graph, f, "S", "G"
)

print("=== CONFIGURATION 1: Uniform Cost Search (UCS) ===")
print(f"Resolved Path:      {' -> '.join(ucs_route)}")
print(f"Accumulated Cost:   {ucs_total_weight}")
print(f"Expansion Log:      {', '.join(ucs_nodes_log)}")
print(f"Expansion Count:    {ucs_total_expansions}\n")

print("=== CONFIGURATION 2: A* Graph Search ===")
print(f"Resolved Path:      {' -> '.join(astar_route)}")
print(f"Accumulated Cost:   {astar_total_weight}")
print(f"Expansion Log:      {', '.join(astar_nodes_log)}")
print(f"Expansion Count:    {astar_total_expansions}")