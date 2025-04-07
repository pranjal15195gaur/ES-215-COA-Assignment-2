import json

def load_dependency_graph(file_path):
    """Load the dependency graph from a JSON file."""
    with open(file_path) as f:
        return json.load(f)

def compute_max_depth(module, dep_graph, visited=None):
    """
    Recursively compute the maximum depth of dependencies for a module.
    `visited` is used to avoid cycles.
    """
    if visited is None:
        visited = set()
    # Add the current module to the visited set
    visited.add(module)
    
    # If the module has no dependencies or is not in the graph, its depth is 0.
    if module not in dep_graph or not dep_graph[module]:
        return 0

    depths = []
    for dep in dep_graph[module]:
        if dep not in visited:
            # Add 1 for the current dependency link plus the depth from that dependency.
            depth = 1 + compute_max_depth(dep, dep_graph, visited.copy())
            depths.append(depth)
        else:
            # If we've encountered a cycle, we do not continue further.
            depths.append(0)
    return max(depths, default=0)

def assess_dependency_depth(dep_graph):
    """
    Assess the maximum dependency depth for each module in the graph.
    """
    depth_results = {}
    for module in dep_graph:
        depth = compute_max_depth(module, dep_graph)
        depth_results[module] = depth
    return depth_results

def main():
    # Ensure that dependencies.json contains the dependency graph for the pelican repository.
    dep_graph = load_dependency_graph('dependency_graph.json')
    
    # Assess the depth of dependencies.
    depth_results = assess_dependency_depth(dep_graph)
    
    print("Dependency Depth per Module:")
    for module, depth in depth_results.items():
        print(f"{module}: depth {depth}")

if __name__ == "__main__":
    main()


