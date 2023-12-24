"""
*****************************PRACRICE 4***************************************
"""

from heapq import heappush as push, heappop as pop
import math

class Graph(object):
    """
    that class uses graphs
    that kind of objects are dictionaries with:
        keys: as the nodes of a graph
        values: a list of edges as tuples
    """

    def __init__(self):
        """
        that method creates an empty graph
        """
        self.matrix = {}

    def add_node(self, node):
        """
        that method adds a node to a graph
        """
        if node not in self.matrix.keys():
            self.matrix[node] = []

    def add_edge(self, source, tarjet, cost):
        """
        that method adds an edge to a graph
        """
        self.add_node(source)
        self.add_node(tarjet)
        self.matrix[source].append((tarjet, cost))

    def nodes(self):
        """
        that method returns a list of the nodes of a graph
        """
        return list(self.matrix.keys())

    def __len__(self):
        """
        that method returns the number of nodes of a graph
        """
        return len(self.matrix)

    def nodes_from_node(self, node):
        """
        that method returns a list of the nodes where you can arrive from a gift node
        """
        if node not in self.nodes():
            raise Exception("Node '" + node + "' not in graph")
        else:
            result = []
            for element in self.matrix[node]:
                if element[0] not in result:
                    result.append(element[0])
            return result

    def edges_from_node(self, node):
        """
        that method returns a list of the edges where you can arrive from a gift node
        """
        if node not in self.nodes():
            raise Exception("Node '" + node + "' not in graph")
        else:
            result = []
            for element in self.matrix[node]:
                result.append((node, element[0], element[1]))
            return result

    def nodecost_from_node(self, node):
        """
        that method returns a list of the edges where you can arrive from a gift node
        and also the appropriate cost
        """
        if node not in self.nodes():
            raise Exception("Node '" + node + "' not in graph")
        else:
            return self.matrix[node]

    def nodes_to_node(self, node):
        """
        that method returns a list of the nodes where you are able to arrive to a gift node
        """
        if node not in self.nodes():
            raise Exception("Node '" + node + "' not in graph")
        else:
            result = []
            for nodo in self.nodes():
                for destino in self.edges_from_node(nodo):
                    if destino == node:
                        result.append(nodo)
                        break
            return result

    @staticmethod
    def from_file(file):
        """
        that static method creates a graph from a file where the edges are written
        as tuples (source, target, cost)
        """
        graph = Graph()
        python_file = open(file).readlines()
        for lst in python_file:
            source = lst.split(",")[0].strip()
            target = lst.split(",")[1].strip()
            cost = lst.split(",")[2].strip()
            graph.add_edge(source, target, cost)
        return graph

    def not_oriented(self):
        """
        that auxiliary method returns the not oriented version of an oriented graph,
        being doubly connected every pair of nodes simply connected
        """
        for node in self.nodes():
            for tupla in self.matrix[node]:
                self.add_edge(tupla[0], node, None)

    def component_of(self, node):
        """
        that method returns a list of the nodes where you can arrive following edges
        from a gift node
        """
        usadas = [node]
        self.not_oriented()
        for node in usadas:
            for i in self.nodes_from_node(node):
                if not i in usadas:
                    usadas.append(i)
        return usadas

def djikstra(graph, source):
    """
    that auxiliary function returns a dictionary with the shortest roads to the node
    source from every node
    """
    dist = {}
    fringe = [(0, None, source)]
    while len(fringe) > 0:
        (dist_to, ant, node) = pop(fringe)
        if node not in dist:
            dist[node] = [ant, dist_to]
            for target, value in graph.nodecost_from_node(node):
                if value != None:
                    push(fringe, (dist_to + int(value), node, target))
    return dist

def rotacion(lista):
    """
    that auxiliary function returns the rotation of a list, being the first the last
    """
    i = 0
    while i < len(lista) // 2:
        lista[i], lista[len(lista) - 1 - i] = lista[len(lista) - 1 - i], lista[i]
        i += 1
    return lista

def min_path(graph, source, target):
    """
    that function returns a tuple with:
        the cost of the road from source to target
        the list of the nodes in the road from source to target
    """
    if source in djikstra(graph, source) and target in djikstra(graph, source):
        diccionario = djikstra(graph, source)
        node = target
        nodelist = [target]
        while node != source:
            node = diccionario[node][0]
            nodelist.append(node)
        return(diccionario[target][1], rotacion(nodelist))
    return math.inf, []
