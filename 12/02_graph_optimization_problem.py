class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """
        srcとdestはどちらもNodeオブジェクトとする
        """
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName()+'->'+self.dest.getName()


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        """
        重み付き枝
        srcとdestはNodeオブジェクトであるとし、weightは数とする
        """
        self.src = src
        self.dest = dest
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.getName()+'->('+str(self.weight)+')'+self.dest.getName()


class Digraph(object):
    """
    nodesはNodeオブジェクトのリストである
    edgesは各nodeを、そのnodeの子ノードのリストにマップする辞書である
    """

    def __init__(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSouece()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node no in graph')
        self.edges[src].append(dest)

    def chilrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result+src.getName()+'->'\
                    + dest.getName()+'\n'
        return result[:-1]  # 最後の改行を省く


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
