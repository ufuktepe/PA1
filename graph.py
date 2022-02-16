import math


class Graph:
    def __init__(self, num_vertices):
        self.n = num_vertices
        self.edges = []

    def get_avg_weight(self):
        sum = 0
        count = 0
        for edge in self.edges:
            sum += edge.weight
            count += 1
        return sum / count




class Edge:
    def __init__(self, v1, v2, w):
        self.vertex_1 = v1
        self.vertex_2 = v2
        self.weight = w


class Vertex1D:
    def __init__(self, v_id):
        self.id = v_id
        self.parent = self
        self.rank = 0


class Vertex2D:
    def __init__(self, v_id, x, y):
        self.id = v_id
        self.x = x
        self.y = y
        self.parent = self
        self.rank = 0

    def get_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Vertex3D:
    def __init__(self, v_id, x, y, z):
        self.id = v_id
        self.x = x
        self.y = y
        self.z = z
        self.parent = self
        self.rank = 0

    def get_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)


class Vertex4D:
    def __init__(self, v_id, x, y, z, t):
        self.id = v_id
        self.x = x
        self.y = y
        self.z = z
        self.t = t
        self.parent = self
        self.rank = 0

    def get_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2 + (self.t - other.t)**2)


if __name__ == '__main__':
    v1 = Vertex2D(4, 0, 0)
    v2 = Vertex2D(6, 3, 4)


    print(v2.get_distance(v1))

