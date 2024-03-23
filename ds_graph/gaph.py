class NodeNotFoundError(Exception):
    """Exception raised when a node is not found in the graph."""
    def __init__(self, node, message="Node not found in graph"):
        self.node = node
        self.message = f"{message}: {node}"
        super().__init__(self.message)


class Graph:
    def __init__(self):
        self.adjacentList = {}

    def addVertex(self, node):
        self.adjacentList[node] = []

    def addEdge(self, node1, node2):
        if node1 not in self.adjacentList:
            raise NodeNotFoundError(node1)
        if node2 not in self.adjacentList:
            raise NodeNotFoundError(node2)

        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnections(self):
        allNodes = self.adjacentList.keys()
        for node in allNodes:
            nodeConnections = self.adjacentList[node]
            connections = ""
            for vertex in nodeConnections:
                connections += vertex + " "
            print(node + "-->" + connections)


if __name__ == "__main__":
    myGraph = Graph()
    myGraph.addVertex('0')
    myGraph.addVertex('1')
    myGraph.addVertex('2')
    myGraph.addVertex('3')
    myGraph.addVertex('4')
    myGraph.addVertex('5')
    myGraph.addVertex('6')
    myGraph.addEdge('3', '1')
    myGraph.addEdge('3', '4')
    myGraph.addEdge('4', '2')
    myGraph.addEdge('4', '5')
    myGraph.addEdge('1', '2')
    myGraph.addEdge('1', '0')
    myGraph.addEdge('0', '2')
    myGraph.addEdge('6', '5')

    myGraph.showConnections()
