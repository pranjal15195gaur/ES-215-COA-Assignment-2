import json
import networkx as nx
# Load dependency graph
with open('dependency_graph.json') as f:
    dep_graph = json.load(f)

# Create a directed graph
G = nx.DiGraph()
for module, dependencies in dep_graph.items():
    for dep in dependencies:
        G.add_edge(module, dep)

# Detect cycles
cycles = list(nx.simple_cycles(G))
if cycles:
    print("Cyclic dependencies detected:")
    for cycle in cycles:
        print(" -> ".join(cycle))
else:
    print("No cyclic dependencies found.")