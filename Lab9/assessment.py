import json
import networkx as nx
from collections import defaultdict

def load_dependency_graph(file_path):
    """Load the dependency graph from a JSON file."""
    with open(file_path) as f:
        return json.load(f)

def build_dependency_graph(dep_graph_data):
    """
    Build a directed dependency graph.
    An edge from A to B indicates that A depends on B.
    """
    G = nx.DiGraph()
    for module, dependencies in dep_graph_data.items():
        for dep in dependencies:
            G.add_edge(module, dep)
    return G

def build_reverse_graph(G):
    """
    Build the reverse of the dependency graph.
    In the reverse graph, an edge from A to B indicates that A is depended upon by B.
    """
    return G.reverse(copy=True)

def get_impacted_modules(core_module, reverse_graph):
    """
    Get all modules that are impacted by changes in the core module.
    These are the modules that (directly or indirectly) depend on the core module.
    """
    impacted = nx.descendants(reverse_graph, core_module)
    return impacted

def compute_fan_in(dep_graph_data):
    """
    Compute the fan-in (number of incoming dependencies) for each module.
    """
    fan_in = defaultdict(int)
    for module, dependencies in dep_graph_data.items():
        for dep in dependencies:
            fan_in[dep] += 1
    return fan_in

def risk_assessment(dep_graph_data, threshold=5):
    """
    Identify modules that are at risk if modified.
    At-risk modules are those with a high fan-in (many modules depend on them).
    Adjust the threshold as necessary.
    """
    fan_in = compute_fan_in(dep_graph_data)
    at_risk = {module: count for module, count in fan_in.items() if count >= threshold}
    return at_risk

def main():
    # Load dependency graph for pelican (ensure dependencies.json is generated from pydeps)
    dep_graph_data = load_dependency_graph('dependency_graph.json')
    
    # Build the dependency graph (direction: A -> B means A depends on B)
    G = build_dependency_graph(dep_graph_data)
    
    # Build the reverse dependency graph (for impact analysis)
    reverse_G = build_reverse_graph(G)
    
    # ----- Impact Assessment -----
    # How would changes in the core module affect the system?
    # Replace "pelican" with the actual core module name if needed.
    core_module = "aiohttp"
    impacted_modules = get_impacted_modules(core_module, reverse_G)
    print(f"Modules impacted by changes in '{core_module}':")
    for module in impacted_modules:
        print(f" - {module}")
    
    # ----- Risk Assessment -----
    # Which modules are at risk of breaking the system if modified?
    # Here, we flag modules with a fan-in greater than or equal to a chosen threshold.
    risk_threshold = 5  # Adjust threshold based on your project scale.
    at_risk_modules = risk_assessment(dep_graph_data, threshold=risk_threshold)
    print("\nModules at risk of breaking the system if modified (high fan-in):")
    for module, count in at_risk_modules.items():
        print(f" - {module}: fan-in = {count}")

if __name__ == "__main__":
    main()


