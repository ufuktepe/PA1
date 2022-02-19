from graph import *
import random
from time import time


def kruskal(graph):

    graph.edges.sort(key=lambda x: x.weight)

    mst = Graph(graph.n)

    max_edge_cost = 0

    i, num_edges = 0, 0

    while num_edges < graph.n - 1:
        edge = graph.edges[i]

        vertex_1 = edge.vertex_1
        vertex_2 = edge.vertex_2

        if find_set(vertex_1) != find_set(vertex_2):
            union(vertex_1, vertex_2)
            mst.edges.append(edge)
            num_edges += 1

            # Update max edge cost
            if max_edge_cost < edge.weight:
                max_edge_cost = edge.weight

        i += 1

        # if i % 100 == 0:
        #     print(i)

    return mst, max_edge_cost


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

    n_list = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]

    print('n,Graph creation runtime,Avg Cost,Max Edge Cost,MST Runtime')

    for n in n_list:
        for i in range(3):
            start = time()

            # Create graph for Kruskal's algorithm
            g = Graph(n)
            vertices = {}

            # Create vertices
            for i in range(n):
                vertices[i] = Vertex1D(i)

            # Create edges
            for i in range(n-1):
                for j in range(i+1, n):
                    w = random.uniform(0, 1)
                    g.edges.append(Edge(vertices[i], vertices[j], w))

            graph_creation_runtime = round(time() - start)

            # Run MST using Kruskal's algorithm
            start = time()
            kruskal_mst, max_edge_cost = kruskal(g)
            mst_runtime = round(time() - start)
            print(f'{n},{graph_creation_runtime},{kruskal_mst.get_avg_weight()},{max_edge_cost},{mst_runtime}')


    print('DONE!')