import networkx as nx
from kruskal import *


def test_kruskal(n):
    start = time()

    # Create graph for Kruskal's algorithm
    my_graph = Graph(n)
    vertices = {}

    # Create Networkx graph
    G = nx.Graph()

    # Create vertices
    for i in range(n):
        G.add_node(i)
        vertices[i] = Vertex1D(i)

    # Create edges
    for i in range(n-1):
        for j in range(i+1, n):
            w = random.uniform(0, 1)
            G.add_edge(i, j, weight=w)
            my_graph.edges.append(Edge(vertices[i], vertices[j], w))

    print(f'Graph building runtime: {time() - start} \n')

    # Run MST using Networkx
    start = time()
    mst = nx.algorithms.minimum_spanning_edges(G, algorithm="kruskal", data=True)
    sum = 0
    for edge in mst:
        sum += edge[2]['weight']
    print(f'Networknx total cost: {sum}')
    print(f'Networknx runtime: {time() - start} \n')

    # Run MST using Kruskal's algorithm
    start = time()
    kruskal_mst, max_edge_cost = kruskal(my_graph)
    print(f'My MST total cost: {kruskal_mst.get_sum_weight()}')
    print(f'My MST runtime: {time() - start}')


if __name__ == '__main__':
    test_kruskal(n=1000)
