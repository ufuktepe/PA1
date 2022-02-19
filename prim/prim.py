from vertex import *
from min_heap import MinHeap
import random
from time import time


def prim(vertices):

    root = vertices[0]
    root.key = 0

    # Create a minimum priority queue
    min_pq = MinHeap(vertices)

    # Total cost of the MST
    cost = 0

    max_edge_cost = 0

    # count = 0
    # n = len(vertices)

    while min_pq.items:

        # Extract the minimum item
        min_item = min_pq.extract_min()

        cost += min_item.key

        # Update max edge cost
        if max_edge_cost < min_item.key:
            max_edge_cost = min_item.key

        # iterate over the adjacent vertices
        for v, weight in min_item.adj.items():
            if v in min_pq.idx_dict and v.key > weight:
                v.key = weight

                # Find the index of v in the heap and decrease its key value.
                v_idx = min_pq.idx_dict[v]
                min_pq.heap_decrease_key(v_idx, weight)

        # count += 1
        # if count % 100 == 0:
        #     print(f'n={n} {count*100//n}%')

    return cost, max_edge_cost


if __name__ == '__main__':

    n_list = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]

    for n in n_list:
        for i in range(3):
            start = time()

            # Vertices for Prim's algorithm
            vertices = []

            # Create vertices
            for i in range(n):
                vertices.append(Vertex1D(i))

            # Create edges
            for i in range(n-1):
                for j in range(i+1, n):
                    w = random.uniform(0, 1)
                    vertices[i].add_adj_vertex(vertices[j], w)

            print(f'n={n} Graph building runtime: {time() - start}')

            # Run MST using Prim's algorithm
            start = time()
            total_cost, max_edge_cost = prim(vertices)
            print(f'Average Cost: {total_cost/n}')
            print(f'Max Edge Cost: {max_edge_cost}')
            print(f'Runtime: {time() - start}\n')

    print('DONE!')

