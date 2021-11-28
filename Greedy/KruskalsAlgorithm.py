class Kruskals:
    """
    First we point every node pointing to itself by -1. Then we go through the
    graph and take the minimum edge one and check if there is any cycle by
    finding the parent by checking it is below zero or not then if we winf that
    both has different parent then we make a union of them.
    Union: We do union by findign the parent of both the node and comparing
    which one has the less value and make it as parent then putting the
    parent's index as other's value.
    """

    def __init__(self, vertices) -> None:
        self.v = vertices
        self.graph = []
        self.parent = [-1] * vertices

    def addEdge(self, src, dst, weight) -> None:
        self.graph.append([src, dst, weight])

    def find(self, node):
        if self.parent[node] < 0:
            return node
        else:
            return self.find(self.parent[node])

    def union(self, a, b):
        ta = self.find(a)
        tb = self.find(b)
        if self.parent[ta] < self.parent[tb]:
            self.parent[ta] = self.parent[ta] + self.parent[tb]
            self.parent[tb] = ta
        else:
            self.parent[tb] = self.parent[ta] + self.parent[tb]
            self.parent[ta] = tb

    def kruskalsSolve(self):
        MST = []
        self.graph = sorted(self.graph, key=lambda item: item[2])
        for src, dst, weight in self.graph:
            x = self.find(src)
            y = self.find(dst)
            if x != y:
                MST.append([src, dst, weight])
                self.union(src, dst)

        self.printMST(MST)

    def printMST(self, MST) -> None:
        for src, dst, weight in MST:
            print("{} - {} -- {}".format(src, dst, weight))


obj = Kruskals(4)
obj.addEdge(0, 1, 10)
obj.addEdge(0, 2, 6)
obj.addEdge(0, 3, 5)
obj.addEdge(1, 3, 15)
obj.addEdge(2, 3, 4)

obj.kruskalsSolve()
