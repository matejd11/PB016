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

    problem.printChild()

    
if __name__ == '__main__':
    main()