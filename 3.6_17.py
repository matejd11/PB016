class Graph(object):

    def __init__(self, graph_dict={}):
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def getGraph(self):
        return self.__graph_dict

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def bfs(self, graph, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in graph.getGraph()[node]:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

def main():

    g = { "a" : ["b", "c"],
            "b" : ["d", "e", "a"],
            "c" : ["d", "e", "a"],
            "d" : ["f", "c", "b"],
            "e" : ["f", "b", "c"],
            "f" : ["d", "e"]
        }

    graph = Graph(g)
    print(graph.bfs(graph, "a", "e"))


if __name__ == '__main__':
    main()