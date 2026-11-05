FOUND = "FOUND"
CUTOFF = "CUTOFF"
FAILURE = "FAILURE"

graph = {"A":["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":["G"],"F":[],"G":[]}

def dls(node, goal, limit, path, visited_path):
    if node == goal:
        return FOUND, path
    if limit == 0:
        return CUTOFF, None
    
    cutoff_occurred = False
    for neighbor in graph.get(node, []):
        if neighbor not in visited_path:
            visited_path.add(neighbor)
            result, found_path = dls(neighbor, goal, limit - 1, path + [neighbor], visited_path)
            visited_path.remove(neighbor)
            
            if result == FOUND:
                return FOUND, found_path
            elif result == CUTOFF:
                cutoff_occurred = True
                
    return (CUTOFF, None) if cutoff_occurred else (FAILURE, None)

def run_dls_wrapper(start, goal, limit):
    return dls(start, goal, limit, [start], {start})

def iddfs(start, goal, max_depth):
    print(f"--- Running IDDFS up to max_depth {max_depth} ---")
    for depth in range(max_depth + 1):
        status, path = run_dls_wrapper(start, goal, depth)
        print(f"Attempted Limit {depth}: Status={status}, Path={path}")
        if status == FOUND:
            return status, path, depth
    return status, None, max_depth

print("=== RUNNING DLS EXPERIMENTS ===")
for limit in [1, 2, 3, 4]:
    status, path = run_dls_wrapper("A", "G", limit)
    print(f"DLS Limit {limit}: Status={status}, Path={path}")

print("\n=== RUNNING IDDFS EXPERIMENTS ===")
for max_depth in [1, 2, 3, 4]:
    iddfs("A", "G", max_depth)
    print()