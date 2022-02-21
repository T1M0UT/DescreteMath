import networkx as nx

def prim(graph):
    """
    Args:
        graph (nx.Graph): a grapth (class networkx.Graph)
    Returns:
        a graph: a minimum spanning tree with minimum weight using Prim's algorithm (class networkx.Graph)
    >>> prim(nx.Graph([(1,2,{'weight':7}),(1,3,{'weight':0}),(2,3,{'weight':1})])).edges(data=True)
    EdgeDataView([(1, 3, {}), (3, 2, {})])
    """
    tree = nx.Graph()
    nodes = list(graph.nodes())
    start_node = nodes[0]
    n = 0
    vertices = set([start_node])
    while n < len(nodes) - 1:
        incident = graph.edges(vertices, data=True)
        choose_low = sorted(incident, key=lambda x: x[2]["weight"])
        choice = choose_low[0][:2]
        i = 0
        while choice[0] in vertices and choice[1] in vertices:
            i +=1
            choice = choose_low[i][:2]
        tree.add_edge(choice[0], choice[1])
        graph.remove_edge(choice[0], choice[1])
        choice = set(choice)
        vertices |= choice
        n += 1
    return tree

