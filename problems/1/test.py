import random
import networkx as nx
from solve import brute_force, binary_search

MAX_N = 20  # Maximum number of nodes
MAX_E = 40  # Maximum number of edges

def generate_case():
    """Generate a random directed graph case."""
    num_nodes = random.randint(10, MAX_N)
    edges = set()

    # Randomly generate edges
    while len(edges) < random.randint(20, MAX_E):
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v:  # Avoid self-loops
            edges.add((u, v))

    graph = nx.DiGraph()
    graph.add_edges_from(edges)
    
    return graph

def generate_test(num_cases):
    """Generate multiple test cases for the Feedback Edge Set problem."""
    tests = []
    
    for _ in range(num_cases):
        case = generate_case()
        tests.append(case)

    return tests

if __name__ == "__main__":
    test_cases = generate_test(10)  # Generate 10 test cases
    for i, graph in enumerate(test_cases):
        a = brute_force(graph)
        b = binary_search(graph)
        print("Minimum set of edges to remove (brute force):", a)
        print("Minimum size of the edge set to remove (binary search):", b)
        print(a == b)