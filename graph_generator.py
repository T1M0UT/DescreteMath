import random
import string
import networkx as nx
import matplotlib.pyplot as plt
import kruskal 
import prim 

from itertools import combinations, groupby

def gnp_random_connected_graph(num_of_nodes: int,
                               completeness: int,
                               draw: bool = False):
    """
     -> list[tuple[int, int]]
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """

    edges = combinations(range(num_of_nodes), 2)
    G = nx.Graph()
    G.add_nodes_from(range(num_of_nodes))
    
    for _, node_edges in groupby(edges, key = lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < completeness:
                G.add_edge(*e)
                
    for (u,v,w) in G.edges(data=True):
        w['weight'] = random.randint(0,10)
                
    if draw: 
        plt.figure(figsize=(10,6))
        nx.draw(G, node_color='lightblue', 
            with_labels=True, 
            node_size=500)
    
    return G

def main():
    """
    Tests efficiency of the algorithms.
    """
    print("Enter a number of nodes: ")
    nodes = int(input(">>> "))

    print("Enter completeness of the graph: ")
    completeness = int(input(">>> "))

    print("Enter number of iterations: ")
    iterations = int(input(">>> "))

    import time
    total_kr = 0
    total_pr = 0
    for _ in range(iterations):
        g = gnp_random_connected_graph(nodes, completeness)
        start = time.time()
        kruskal.kruskal(g)
        end = time.time()
        total_kr += end - start

        start = time.time()
        prim.prim(g)
        end = time.time()
        total_pr += end - start

    prim_time = total_pr/iterations
    kruskal_time = total_kr/iterations

    print("Prim's algorithm: " + str(prim_time))
    print("Kruskal's algorithm: " + str(kruskal_time))
    print("Difference: " + str(prim_time - kruskal_time))


if __name__ == "__main__":
    main()
