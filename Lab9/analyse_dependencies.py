import json
import networkx as nx

# Load the dependency graph from JSON file
with open("dependency_graph.json", "r") as f:
    data = json.load(f)

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph based on dependencies
for module, dependencies in data.items():
    for dep in dependencies:
        G.add_edge(module, dep)

# ---- (1) Identify Highly Coupled Modules ----
fan_in = {node: G.in_degree(node) for node in G.nodes()}
fan_out = {node: G.out_degree(node) for node in G.nodes()}

most_dependent = sorted(fan_in.items(), key=lambda x: x[1], reverse=True)[:5]  # Top 5 fan-in
most_dependent_on = sorted(fan_out.items(), key=lambda x: x[1], reverse=True)[:5]  # Top 5 fan-out

print("\n🔍 Highly Coupled Modules:")
print("Most Depended-On Modules (High Fan-In):", most_dependent)
print("Modules That Depend on Many Others (High Fan-Out):", most_dependent_on)

# ---- (2) Detect Cyclic Dependencies ----
cycles = list(nx.simple_cycles(G))

if cycles:
    print("\n⚠️ Cyclic Dependencies Found:")
    for cycle in cycles:
        print(" -> ".join(cycle))
else:
    print("\n✅ No Cyclic Dependencies Detected")

# ---- (3) Find Unused and Disconnected Modules ----
unused_modules = [node for node in G.nodes() if G.in_degree(node) == 0 and G.out_degree(node) == 0]
disconnected_modules = list(nx.isolates(G))  # Nodes with no connections

print("\n🛑 Unused Modules:", unused_modules)
print("🛑 Disconnected Modules:", disconnected_modules)

# ---- (4) Assess Depth of Dependencies ----
longest_path_length = 0
longest_path = []

for node in G.nodes():
    for other_node in G.nodes():
        if node != other_node and nx.has_path(G, node, other_node):
            path_length = nx.shortest_path_length(G, node, other_node)
            if path_length > longest_path_length:
                longest_path_length = path_length
                longest_path = nx.shortest_path(G, node, other_node)

print("\n📏 Longest Dependency Chain Length:", longest_path_length)
print("📏 Longest Dependency Path:", " -> ".join(longest_path))
