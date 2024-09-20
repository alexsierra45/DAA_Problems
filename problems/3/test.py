import networkx as nx
import random
from solve import solve

MAX_NODE_NUMBER=10**3
MAX_NODE_VALUE=2**32

def generate_case():
    global MAX_NODE_NUMBER
    global MAX_NODE_VALUE
    return [random.randint(0, MAX_NODE_VALUE) for _ in range(random.randint(0, MAX_NODE_NUMBER))]

def solve_test(case):
    def active_lsb(num):
        # Verificar si el número es cero
        if num == 0:
            return None  # No hay bits activos en cero

        # Encontrar el LSB activo
        lsb = num & -num
        return lsb
    
    # Crear un grafo no dirigido
    G = nx.Graph()
    # Definir el número de nodos
    num_nodes = len(case)
    # Añadir nodos
    G.add_nodes_from(range(num_nodes))
    # Añadir aristas con pesos aleatorios
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = active_lsb(case[i] & case[j])
            if weight is not None:
                G.add_edge(i, j, weight=weight)

    # Encontrar el árbol abarcador de costo mínimo usando el algoritmo de Prim
    T = nx.minimum_spanning_tree(G)

    # Calcular la suma de los pesos de las aristas del MST
    total_weight = sum(weight for _, _, weight in T.edges(data='weight'))

    return total_weight

def generate_test(num):
    a = []
    for _ in range(num):
        b = generate_case()
        a.append((b, solve_test(b)))
    accuracy = 0
    for t, ans in a:
        if solve(t) == ans:
            accuracy += 1
    print(f'Accuracy of {accuracy / num * 100}% for {num} tests cases')

generate_test(100)