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

    def get_sum_weight(self):
        sum = 0
        for edge in self.edges:
            sum += edge.weight
        return sum


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


class Vertex2D(Vertex1D):
    def __init__(self, v_id, x, y):
        super(Vertex2D, self).__init__(v_id)
        self.x = x
        self.y = y

    def get_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Vertex3D(Vertex2D):
    def __init__(self, v_id, x, y, z):
        super(Vertex3D, self).__init__(v_id, x, y)
        self.z = z

    def get_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)


class Vertex4D(Vertex3D):
    def __init__(self, v_id, x, y, z, t):
        super(Vertex4D, self).__init__(v_id, x, y, z)
        self.t = t

    def get_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2 + (self.t - other.t)**2)


if __name__ == '__main__':
    pass

