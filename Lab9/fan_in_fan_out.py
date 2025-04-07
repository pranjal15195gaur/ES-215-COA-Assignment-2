import json
from collections import defaultdict
# Load the dependency graph
with open('dependency_graph.json') as f:
    # The JSON structure might differ; adjust the keys accordingly.
    # This example assumes a structure like: { "module1": ["dep1", "dep2", ...], ... }
    dep_graph = json.load(f)

fan_out = {} # Direct dependencies for each module.
fan_in = defaultdict(int) # Count of modules depending on each module.

for module, dependencies in dep_graph.items():
    fan_out[module] = len(dependencies)
    for dep in dependencies:
        fan_in[dep] += 1

# Display the fan-out values.
print("Fan-Out (dependencies per module):")
for module, count in fan_out.items():
    print(f"{module}: {count}")
    
# Display the fan-in values.
print("\nFan-In (dependent modules count):")
for module, count in fan_in.items():
    print(f"{module}: {count}")