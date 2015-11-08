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


    def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not (start in graph.vertices()):
            return None
        for node in graph.getGraph()[start]:
            if node not in path:
                newpath = Graph.find_path(graph, node, end, path)
                if newpath: 
                    return newpath
        return None

    def find_all_paths(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            yield path
        if not (start in graph.vertices()):
            return None
        for node in graph.getGraph()[start]:
            if node not in path:
                newpath = self.find_all_paths(graph, node, end, path)
                if newpath:
                    yield from newpath
        return None

    def find_shortest_path(self, graph, start, end, path=[]):
        best = None
        for x in graph.find_all_paths(graph, "a", "f"):
            if best is None or len(x) < len(best):
                best = x
        return best


def main():
    g = { "a" : ["b", "c"],
            "b" : ["d", "e", "a"],
            "c" : ["d", "e", "a"],
            "d" : ["f", "c", "b"],
            "e" : ["f", "b", "c"],
            "f" : ["d", "e"]
        }

    graph = Graph(g)
    print(graph.find_shortest_path(graph, "a", "f"))

if __name__ == '__main__':
    main()