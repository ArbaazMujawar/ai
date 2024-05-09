# Importing deque from collections module (not used in the code)
from collections import deque

# Defining a Graph class
class Graph:
    def __init__(self, adjacency_list):
        # Initializing the adjacency list of the graph
        self.adjacency_list = adjacency_list
    
    # Method to get neighbors of a node
    def get_neighbors(self, v):
        return self.adjacency_list[v]
    
    # Heuristic function h(n) - returns heuristic values for nodes
    def h(self, n):
        # Heuristic values for nodes A, B, C, D
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }
        return H[n]
    
    # A* algorithm implementation to find shortest path
    def a_star_algorithm(self, start_node, stop_node):
        # Initializing open list, closed list, g values, and parent nodes
        open_list = set([start_node])
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node
        
        # A* algorithm main loop
        while len(open_list) > 0:
            n = None
            # Selecting the node with the lowest f value from open list
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v
            # If no path exists, print and return None
            if n == None:
                print('Path does not exist!')
                return None
            # If the goal node is reached, reconstruct and print the path
            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                return reconst_path
            
            # Iterating through neighbors of current node
            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)
            # Removing the current node from open list and adding to closed list
            open_list.remove(n)
            closed_list.add(n)
        
        # If no path found, print and return None
        print('Path does not exist!')
        return None

# Adjacency list representation of the graph
adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

# Creating an instance of the Graph class with the adjacency list
graph1 = Graph(adjacency_list)

# Calling the A* algorithm method to find the shortest path from 'A' to 'D'
graph1.a_star_algorithm('A', 'D')