class Node():

    def __init__(self, name, typ):
        self.name = name
        self.typ = typ
        self.childs = []

    def addChild(self, node):
        self.childs.append(node)

    def printChild(self, tab = 0):
        print("  "*tab + self.name + "*"*(self.typ == "end"))
        for i in self.childs:
            i.printChild(tab+1)

    def printSol(self, sol, tab = 0):
        if self.name in sol:
            print("  "*tab + self.name + "*"*(self.typ == "end"))
            for i in self.childs:
                i.printSol(sol, tab+1)

def solve(problem, result = []):

    if problem.typ == "end":
        return True, result + [problem.name]

    if problem.typ == "":
        return False, []

    if problem.typ == "and":
        a = []
        for node in problem.childs:
            res, ress = solve(node)
            if res == False:
                return False, []
            else:
                a += ress
                pass
        return True, ress + a + [problem.name]

    if problem.typ == "or":
        for node in problem.childs:
            res, ress = solve(node)
            if res == True:
                return True, ress + [problem.name]
        return False, []

def main():
    problem = Node("a","or")
    
    b = Node("b","and")
    problem.addChild(b)
    c = Node("c","and")
    problem.addChild(c)
    
    d = Node("d","end")
    b.addChild(d)
    e = Node("e","or")
    b.addChild(e)

    h = Node("h","end")
    e.addChild(h)

    f = Node("f","and")
    c.addChild(f)
    g = Node("g","end")
    c.addChild(g)

    i = Node("i","")
    f.addChild(i)
    f.addChild(h)

    i, sol = solve(problem)
    problem.printSol(sol)

    
if __name__ == '__main__':
    main()