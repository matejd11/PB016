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

    def depth_first_search_limit(self, graph, start, end, path , limit):
        if limit <= 0:
            return None
        path = path + [start]
        if start == end:
            return path

        for node in graph.getGraph()[start]:
            if node not in path:
                res = self.depth_first_search_limit(graph, node, end, path, limit-1)
                if res != None:
                    return res


def main():

    print("Príklad DFS limit")

    g = { "a" : ["b", "c"],
            "b" : ["d", "e", "a"],
            "c" : ["d", "e", "a"],
            "d" : ["f", "c", "b"],
            "e" : ["f", "b", "c"],
            "f" : ["d", "e"]
        }

    graph = Graph(g)
    print(graph.depth_first_search_limit(graph, "a", "e", [], 3))


if __name__ == '__main__':
    main()