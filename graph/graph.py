from node import Node
from code_challeng_stack_and_Queue import Queue
from code_challeng_stack_and_Queue.stack import Stack



class Edge:
    def __init__(self,vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.size = 0
        self.list = []
    # this function to add a node inside Graph #Note for me >> vertex named in Graph that same node name in tree يعني vertex==node 
    def add_node(self, value):
        new_vertex = Node(value)
        #add key to dictionary (self.adj_list[new_vertex]) #this is mean the value for this node empty list= []
        self.adj_list[new_vertex] = []
        self.size+=1
        return new_vertex
    
    def add_edge(self,node1, node2, weight=0):
        #check if this node inside keys in dictionary is exist or not
        if not node1 in self.adj_list.keys():
            return("this node does not exist")
        
        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)

    def neighbors(self,new_vertex,weight=0):
        """Returns a collection of edges connected to the given vertex"""
        output=""
        for edge in self.adj_list[new_vertex]:
            output+= f"{edge.vertex}--->"
        return output
    
    # def vertices(self):
    #     self.list=[]
    #     for vertices in self.adj_list.keys():
    #         self.list.append(vertices.value) 
    #     return self.list
    def vertices(self):
        list=[]
        for vertices in self.adj_list.keys():
            list.append(vertices.value) 
        return list

    def get_size(self):
        if self.adj_list is None:
            return 0
        return self.size
    
    def breadth_first(self, node):
        #Implement a breadth-first traversal on a graph.
        if node not in self.adj_list:
            return []
        visited = []
        queue = Queue()
        result = []  # Create a list to store the visited nodes in order
       
        visited.append(node)
        queue.enqueue(node)
       
       
        while not queue.isEmpty():  # Check if the queue is empty
            m = queue.dequeue()
            result.append(m.value)
            # if m not in visited:
            #     visited.append(m)
            #     result.append(m)  # Append the current node to the result list
            for edge in self.adj_list[m]:
              if edge.vertex not in visited:
                    queue.enqueue(edge.vertex)
                    visited.append(edge.vertex)
       
        return result
    
    
    def Depth_first(self,node):
        if node not in self.adj_list:
            return []
        visited = []
        stack=Stack()
        result=[]
        stack.push(node)
        visited.append(node)
        while not stack.isEmpty():  # Check if the stack is empty
            n=stack.pop()
            result.append(n.value)
            for i in self.adj_list[n]:
                if i.vertex not in visited:
                    stack.push(i.vertex)
                    visited.append(i.vertex)
        return result
    # implementation using adjacency
    def create_adjacency_list(self,vertices, edges):
        adjacency_list = {}
        for i in range(len(vertices)):
            vertex = vertices[i]
            neighbors = []
            for j in range(len(vertices)):
                if edges[i][j]:
                    neighbors.append(vertices[j])
            adjacency_list[vertex] = neighbors
        return adjacency_list
    
    def business_trip(graph, cities):
        total_cost = 0
        for i in range(len(cities) - 1):
            current_city = cities[i]
            next_city = cities[i + 1]
            if current_city not in graph or next_city not in graph[current_city]:
                return None
            total_cost+=graph[current_city][next_city]
        return total_cost

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex} -----> '
            output += '\n'
        return output