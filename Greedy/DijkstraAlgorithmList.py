from collections import defaultdict
from heapq import heappop, heappush


class Dijkstra:
    """
    We create the graph using addEdge. Then we create a minHeap to extract the
    minimum weighted visited vertice. Then we loop through all the adjacency
    vertices and pick the minimum one and put it in the distanceFromSource list
    """

    def __init__(self, vertices) -> None:
        self.v = vertices
        self.graph = defaultdict(list)

    def addEdge(self, src, distanceFromSource, weight) -> None:
        new_node = [distanceFromSource, weight]
        self.graph[src].insert(0, new_node)

        # For undirected
        new_node = [src, weight]
        self.graph[distanceFromSource].insert(0, new_node)

    def dijkstraSolve(self, startNode):
        minHeap = []
        distanceFromSource = [-1] * self.v
        distanceFromSource[startNode] = 0
        heappush(minHeap, (0, startNode))
        while minHeap:
            currentDistance, currentNode = heappop(minHeap)

            if currentDistance > distanceFromSource[currentNode]:
                continue

            for neighbour, weight in self.graph[currentNode]:
                distance = currentDistance + weight

                if distanceFromSource[neighbour] == -1:
                    distanceFromSource[neighbour] = distance
                    heappush(minHeap, (distance, neighbour))

                if distance < distanceFromSource[neighbour]:
                    distanceFromSource[neighbour] = distance
                    heappush(minHeap, (distance, neighbour))

        self.printDijkstra(distanceFromSource)

    def printDijkstra(self, dist):
        print("Vertex\tDistance from source")
        for i in range(self.v):
            print("{}\t\t{}".format(i, dist[i]))


graph = Dijkstra(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.dijkstraSolve(0)
