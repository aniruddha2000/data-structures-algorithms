from sys import maxsize


class Prims:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def primsSolve(self) -> None:
        noOfEdges = 0
        selected = [None] * self.vertices
        selected[0] = True
        while noOfEdges < self.vertices - 1:
            minimum = maxsize
            row, col = 0, 0
            for _row in range(self.vertices):
                if selected[_row]:
                    for _col in range(self.vertices):
                        if (not selected[_col]) and self.graph[_row][_col]:
                            if minimum > self.graph[_row][_col]:
                                minimum = self.graph[_row][_col]
                                row = _row
                                col = _col
            print(str(row) + "-" + str(col) + ":" + str(self.graph[row][col]))
            selected[col] = True
            noOfEdges += 1


prims = Prims(5)
prims.graph = [
    [0, 19, 5, 0, 0],
    [19, 0, 5, 9, 2],
    [5, 5, 0, 1, 6],
    [0, 9, 1, 0, 1],
    [0, 2, 6, 1, 0],
]
print(prims.primsSolve())
