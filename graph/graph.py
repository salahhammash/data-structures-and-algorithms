from node import Node
from code_challeng_stack_and_Queue import Queue


class Edge:
    def __init__(self,vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex
    
    def add_edge(self,node1, node2, weight=0):

        if not node1 in self.adj_list.keys():
            return("this node does not exist")
        
        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex} -----> '
            output += '\n'
        return output
    
    
    def get_vertices(self):
        """Return a list of all vertices in the graph."""
        return self.adj_list.keys()

    def get_neighbours(self, vertex):
        """Return a list of neighbors of a given vertex in the graph."""
        return self.adj_list[vertex]
    
    def get_size(self):
        """Return the number of vertices in the graph."""
        return len(self.adj_list)
    
    def breadth_first(self):
        """ Return: A collection of nodes in the order they were visited."""
        
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            self = queue.get()
            #  The get() method is used to remove and return the item from the front of the queue.
            print(self.info)

            if self.left:
                queue.put(self.left)

            if self.right:
                queue.put(self.right)

    
    
    def business_trip():
        """
    Takes in a graph and a list of cities.
    Return: True or False, depending on whether the trip is possible with direct flights, and how much it would cost.
        """
        pass
    
    
    def Depth_first():
        
        pass