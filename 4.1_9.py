import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

class Graph(object):

    def __init__(self, rawgraph={}):
        """ initializes a graph object """
        self.rawgraph = rawgraph

    def inGraph(self, point):
        x, y = point
        if x >= 0 and x < len(self.rawgraph):
            if y >= 0 and y < len(self.rawgraph[0]):
                return True
        return False

    def neighbors(self, point):
        tmp = []
        x, y = point
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if self.inGraph((x+i, y+j)):
                    if self.rawgraph[x+i][y+j] != 1:
                        tmp.append((x+i, y+j))
        return tmp

    def cost(self, pointA, pointB):
        (x1, y1) = pointA
        (x2, y2) = pointB
        a = abs(x1 - x2) 
        b = abs(y1 - y2)
        if a == b: #skusit ine, rovnake
            return 1
        else:
            return 1

    def heuristic(self, a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def a_star_search(self, start, goal):
        graph = self
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        
        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break
            
            for nextPoint in graph.neighbors(current):
                new_cost = cost_so_far[current] + graph.cost(current, nextPoint)
                if nextPoint not in cost_so_far or new_cost < cost_so_far[nextPoint]:
                    cost_so_far[nextPoint] = new_cost
                    priority = new_cost + graph.heuristic(goal, nextPoint)
                    frontier.put(nextPoint, priority)
                    came_from[nextPoint] = current
        
        self.costs = [
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1]
        ]
        for v in came_from:
            x, y = v
            self.costs[x][y] = cost_so_far[(x,y)]

        self.heur = [
                [-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1]
            ]
        for v in came_from:
            x, y = v
            self.heur[x][y] = self.heuristic(goal, (x,y))


        return came_from, cost_so_far

    def cesta(self, start, ciel, cesta = []):

        #print(cesta, ciel)
        cesta.append(ciel)
        if ciel == start:
            #print("cesta", cesta)
            return cesta[::-1]

        x, y = ciel

        cost = self.costs[x][y]

        for steep in self.neighbors((x, y)):
            #print("steep", steep, cost)
            x1, y1 = steep
            if self.costs[x1][y1] < cost and self.costs[x1][y1] >= 0:
                return self.cesta(start, steep, cesta)
        

def main():

    print("Príklad A*")

    g = [
            [0,0,0,0,0,0],
            [0,0,1,1,0,0],
            [0,0,0,1,0,0],
            [0,0,0,1,0,0],
            [0,0,0,0,0,0]
        ]

    graph = Graph(g)
    a, b = graph.a_star_search((2, 1), (2,5))
    #print(a)
    #print()
    #print(b)

    tmp = [
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1]
        ]
    for v in a:
        x, y = v
        tmp[x][y] = b[(x,y)]

    for x in tmp:
        pass
        #print(x)

    print(graph.cesta((2,1), (2, 5)))

    tmp = [
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1]
        ]
    for v in a:
        x, y = v
        tmp[x][y] = graph.heuristic((2,5),(x,y))

    for x in tmp:
        pass
        #print(x)




if __name__ == '__main__':
    main()