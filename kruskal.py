import networkx as nx

def combine_sets(nodes, edge):
    """
    >>> combine_sets([{1}, {2, 3, 4}, {5, 6}], (1, 5))
    [{1, 5, 6}, {2, 3, 4}]
    >>> combine_sets([{1, 2, 3}, {4}, {5, 6, 7}], (3, 4))
    [{1, 2, 3, 4}, {5, 6, 7}]
    """
    for node_1 in nodes:
        if edge[0] in node_1:
            for node_2 in nodes:
                if edge[1] in node_2:
                    new_node = node_1|node_2 
                    return [new_node] + [node for node in nodes if node != node_1 and node != node_2]


def kruskal(graph):
    """
    Args:
        graph (nx.Graph): a grapth (class networkx.Graph)
    Returns:
        a graph: a minimum spanning tree with minimum weight using Kruskal's algorithm (class networkx.Graph)
    >>> kruskal(nx.Graph([(1,2,{'weight':7}),(1,3,{'weight':0}),(2,3,{'weight':1})])).edges(data=True)
    EdgeDataView([(1, 3, {}), (3, 2, {})])
    """
    tree = nx.Graph()
    edges = sorted(list(graph.edges(data=True)), key=lambda x: x[2]["weight"])
    nodes = [{node} for node in graph.nodes()]
    n = 0
    for edge in edges:
        for node in nodes:
            if (edge[0] in node) and not (edge[1]  in node):
                    tree.add_edge(edge[0], edge[1])
                    nodes = combine_sets(nodes, edge)
                    n += 1
                    if n == len(graph.nodes()) - 1:
                        return tree

    return tree

