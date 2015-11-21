class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

    def delete(self):
        if self.l == self.r == None:
            return None
        if self.l == None:
            return self.r
        if self.r == None:
            return self.l

        child = self.l
        grandchild = child.r
        if grandchild:
            while grandchild.r:
                child = grandchild
                grandchild = child.r
            self.v = grandchild.v
            child.r = grandchild.l
        else:
            self.l = child.l
            self.v = child.v

        return self

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            return self._find(val, node.l)
        elif(val > node.v and node.r != None):
            return self._find(val, node.r)

    def deleteTree(self): 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root, 0)

    def _printTree(self, node, rekurzia):
        if(node != None):
            self._printTree(node.r, rekurzia + 1)
            print(("    " * rekurzia) + str(node.v) + ' ')
            self._printTree(node.l, rekurzia + 1)

    def delete(self, value):
        if self.root and self.root.v == value:
            self.root = self.root.delete()
            return

        else:
            parent = self.root
            while parent:
                if value < parent.v:
                    child = parent.l
                    if child and child.v == value:
                        parent.l = child.delete()
                        return
                    parent = child
                else:
                    child = parent.r
                    if child and child.v == value:
                        parent.r = child.delete()
                        return
                    parent = child


def main():
    print("Príklad na odoberanie uzlu z binárneho stroma:")
    tree = Tree()
    tree.add(8)
    tree.add(3)
    tree.add(7)
    tree.add(5)
    tree.add(2)
    tree.add(4)
    tree.add(1)
    tree.add(6)
    tree.add(9)
    print("original:")
    tree.printTree()
    print()
    tree.delete(7)
    print("odoberieme 7:")
    tree.printTree()
    print()

if __name__ == '__main__':
    main()