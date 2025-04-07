import json
import networkx as nx
from collections import defaultdict

def load_dependency_graph(file_path):
    """Load the dependency graph from a JSON file."""
    with open(file_path) as f:
        return json.load(f)

def calculate_fan_in_out(dep_graph):
    """Calculate the fan-in and fan-out for each module."""
    fan_in = defaultdict(int)
    fan_out = {}
    for module, dependencies in dep_graph.items():
        fan_out[module] = len(dependencies)
        for dep in dependencies:
            fan_in[dep] += 1
    return fan_in, fan_out

def identify_unused_modules(dep_graph, fan_in):
    """Identify modules with no incoming dependencies (potentially unused)."""
    all_modules = set(dep_graph.keys())
    modules_with_incoming = set(fan_in.keys())
    unused_modules = all_modules - modules_with_incoming
    return unused_modules

def main():
    # Load the dependency graph (ensure dependencies.json is in the same directory)
    dep_graph = load_dependency_graph('dependency_graph.json')
    
    # Calculate fan-in and fan-out
    fan_in, fan_out = calculate_fan_in_out(dep_graph)

    # Identify unused modules (modules with no incoming dependencies)
    unused_modules = identify_unused_modules(dep_graph, fan_in)
    if unused_modules:
        print("\nModules with no incoming dependencies (potentially unused):")
        for mod in unused_modules:
            print(mod)
    else:
        print("\nAll modules have at least one incoming dependency.")

if __name__ == "__main__":
    main()
