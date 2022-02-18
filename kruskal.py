from graph import *
import networkx as nx
from random import randint
from time import time


def kruskal(graph):

    graph.edges.sort(key=lambda x: x.weight)

    mst = Graph(graph.n)

    i, num_edges = 0, 0

    while num_edges < graph.n - 1:
        edge = graph.edges[i]

        vertex_1 = edge.vertex_1
        vertex_2 = edge.vertex_2

        if find_set(vertex_1) != find_set(vertex_2):
            union(vertex_1, vertex_2)
            mst.edges.append(edge)
            num_edges += 1

        i += 1

    return mst


def find_set(v):
    """
    Recursively finds the root of the tree containing vertex v.
    :param v: the given vertex
    :return: the root of the tree containing vertex v
    """
    if v.parent != v:
        v.parent = find_set(v.parent)
    return v.parent


def union(v1, v2):
    """
    Finds the roots of the sets containing vertices u and v and combines the two sets. The root with higher rank
    becomes the parent of the root with lower rank. If the two roots have equal rank, one of the roots is chosen
    arbitrarily as the parent and its rank is incremented.
    :param v1: first given vertex
    :param v2: second given vertex
    :return: None
    """
    root_v1 = find_set(v1)
    root_v2 = find_set(v2)

    if root_v1 == root_v2:
        return

    if root_v1.rank > root_v2.rank:
        root_v2.parent = root_v1
    else:
        root_v1.parent = root_v2
        if root_v1.rank == root_v2.rank:
            root_v1.rank += 1


if __name__ == '__main__':
    start = time()
    n = 1000

    my_graph = Graph(n)
    vertices = {}

    G = nx.Graph()

    for i in range(n):
        G.add_node(i)
        vertices[i] = Vertex1D(i)

    for i in range(n-1):
        for j in range(i+1, n):
            w = randint(1, n)
            G.add_edge(i, j, weight=w)
            my_graph.edges.append(Edge(vertices[i], vertices[j], w))

    print(f'Graph Building: {time() - start}')

    # NX
    start = time()
    mst = nx.algorithms.minimum_spanning_edges(G, algorithm="kruskal", data=True)
    edgelist = list(mst)
    sum = 0
    for edge in edgelist:
        sum += edge[2]['weight']
    print(f'Networknx: {sum}')
    print(f'Networknx: {time() - start}')

    # My Algorithm
    start = time()
    my_mst = kruskal(my_graph)
    print(f'My MST: {my_mst.get_sum_weight()}')
    print(f'My MST: {time() - start}')
