import networkx as nx
from itertools import combinations

def brute_force(graph):
    edges = list(graph.edges())
    n = len(edges)
    
    # Test all subsets of edges
    for k in range(n + 1):
        for combination in combinations(edges, k):
            modified_graph = graph.copy()
            modified_graph.remove_edges_from(combination)
            
            if nx.is_directed_acyclic_graph(modified_graph):
                return len(combination)  # Return the first combination that makes the graph acyclic
    
    return None

def binary_search(graph):
    edges = list(graph.edges())
    n = len(edges)

    def can_remove(size):
        for combination in combinations(edges, size):
            modified_graph = graph.copy()
            modified_graph.remove_edges_from(combination)
            if nx.is_directed_acyclic_graph(modified_graph):
                return True
        return False

    left, right = 0, n
    best_size = n

    while left <= right:
        mid = (left + right) // 2
        
        if can_remove(mid):
            best_size = mid  
            right = mid - 1  
        else:
            left = mid + 1 

    return best_size

# Example usage
if __name__ == "__main__":
    G = nx.DiGraph()
    G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4)])  # Directed graph with a cycle

    print("Minimum set of edges to remove (brute force):", brute_force(G))
    print("Minimum size of the edge set to remove (binary search):", binary_search(G))