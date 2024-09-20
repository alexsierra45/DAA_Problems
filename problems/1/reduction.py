import networkx as nx
from networkx import Graph, DiGraph

def vc_reduction(G: Graph) -> DiGraph:
    dG = DiGraph()
    graph_len = len(G)
    for n in G:
        dG.add_nodes_from([n, graph_len + n])
        dG.add_edge(n, graph_len + n)
    for u, v in G.edges():
        dG.add_edges_from([(graph_len + v, u), (graph_len + u, v)])

    return dG

G = Graph()
G.add_nodes_from([1, 2, 3])
G.add_edge(1, 2)
print(vc_reduction(G))