"""
@Author: Abul Kalam Azad

"""

#########################################################################################
# It contains the definition of some function that used for MaxClique implementations   #
#########################################################################################

# Import Packages
import networkx as nx
import matplotlib.pyplot as plt

#########################################################################################
#  1. To generate lower adj_matrix to complete adj_matrix                               #
#########################################################################################
def lower_matrix_complete_matrix(filename):
    # Read the input file and count the number of nodes
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_nodes = len(lines)

    # Create adjacency matrix
    adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]  # Initialize adjacency matrix with zeros
    
    # Populate the adjacency matrix
    for line in lines:
        elements = line.split()  # Split each line into elements
        node_index = int(elements[0])  # Extract the node index
        connections = [int(x) for x in elements[1:]]  # Extract connections for the node
        
        for i, connected in enumerate(connections):
            if connected == 1:  # If there is a connection
                adj_matrix[node_index][i] = 1
                adj_matrix[i][node_index] = 1  # Symmetrically update the upper triangle
    return adj_matrix

#########################################################################################
#  2. To generate lower adj_list to Complete adj_matrix                                 #
#########################################################################################
def lower_list_complete_matrix(filename):
    # Read the input file and count the number of nodes
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_nodes = len(lines)

    # Create adjacency matrix
    adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]  # Initialize adjacency matrix with zeros
    
    # Populate the adjacency matrix
    for node_index, line in enumerate(lines):
        connections = [int(x) for x in line.split()[1:]]  # Extract connections for the node
        
        for connected_node in connections:
            adj_matrix[node_index][connected_node] = 1
            adj_matrix[connected_node][node_index] = 1  # Symmetrically update the upper triangle
    
    return adj_matrix

#########################################################################################
#  3. To generate lower adj_list to complete adj_list                                   #
#########################################################################################
def lower_list_complete_list(filename):
    adj_list = {}
    # Read the input file line by line
    with open(filename, 'r') as file:
        for line in file:
            elements = line.strip().split()  # Split each line into elements
            node = int(elements[0])  # Extract the node index
            connections = [int(x) for x in elements[1:]]  # Extract connections for the node
            #print("\n connections ", connections)
            
            if node not in adj_list:  # Check if node is not in adj_list
                adj_list[node] = connections
            else:
                adj_list[node].extend(connections)  # Extend the existing list

            # Ensure bidirectional connections for the current node
            for conn_node in connections:
                if conn_node not in adj_list:
                    adj_list[conn_node] = [node]
                if node not in adj_list.get(conn_node, []):
                    adj_list.setdefault(conn_node, []).append(node)
    return adj_list

#########################################################################################
#  4. To generate lower adj_matrix to complete adj_list                                 #
#########################################################################################
def lower_matrix_complete_list(filename):
    adj_list = {}
    # Read the input file line by line
    with open(filename, 'r') as file:
        for line in file:
            elements = [int(x) for x in line.strip().split()]  # Convert elements to integers
            node = elements[0]  # Extract the node index
            connections = elements[1:]  # Extract connections
            
            # Ensure bidirectional connections for the current node
            for i, val in enumerate(connections):
                if val == 1:
                    # Update adjacency list for the current node
                    if node not in adj_list:
                        adj_list[node] = []
                    adj_list[node].append(i)

                    # Ensure bidirectional connection
                    if i not in adj_list:
                        adj_list[i] = []
                    if node not in adj_list[i]:
                        adj_list[i].append(node)
    return adj_list
    
#########################################################################################
# 5. To generate lower triangular adj_matrix to complete adj_matrix                     #
# It inserted 1 for row=column (diagonal) position                                      #
# For experiment with 3.clique-using-proposed-alg-6                                     #
#########################################################################################
def lower_matrix_diagonal_complete_matrix(filename):
    # Read the input file and count the number of nodes
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_nodes = len(lines)

    # Create adjacency matrix
    adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]  # Initialize adjacency matrix with zeros
    
    # Populate the adjacency matrix
    for line in lines:
        elements = line.split()  # Split each line into elements
        node_index = int(elements[0])  # Extract the node index
        connections = [int(x) for x in elements[1:]]  # Extract connections for the node
        
        for i, connected in enumerate(connections):
            if connected == 1:  # If there is a connection
                adj_matrix[node_index][i] = 1
                adj_matrix[i][node_index] = 1  # Symmetrically update the upper triangle
    for i in range(len(adj_matrix)):
        adj_matrix[i][i] = 1
    return adj_matrix

#########################################################################################
# 6. To generate Complement adj_matrix                                                  #             
#########################################################################################
def complement_graph(adj_matrix):
    num_nodes = len(adj_matrix)
    complement_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                complement_matrix[i][j] = 1 - adj_matrix[i][j]
    return complement_matrix

#########################################################################################
# 7. To generate Complement adj_list                                                    #             
#########################################################################################
def complement_graph_list(adj_list):
    complement_list = {}
    for u in adj_list:
        complement_list[u] = []
        for v in adj_list:
            if u != v and v not in adj_list[u]:
                complement_list[u].append(v)
    return complement_list

#########################################################################################
# 8. To Draw graph from adj_matrix                                                      #             
#########################################################################################
def draw_graph(adj_matrix):
    graph = nx.Graph()
    num_nodes = len(adj_matrix)
    graph.add_nodes_from(range(num_nodes))
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if adj_matrix[i][j] == 1:
                graph.add_edge(i, j)
    nodes_position = nx.spring_layout(graph)
    nx.draw(graph, nodes_position, with_labels=True, node_size=200, node_color='blue', font_size=8, font_color='white')
    plt.savefig(f"{num_nodes}_nodes_graph.png")
    plt.show()
    #return nodes_position
    
#########################################################################################
# 9. Verify Clique using adj_matrix                                                     #             
#########################################################################################
def clique_verifier(adj_matrix, clique):
    clique_list = list(clique)  # Convert the set to a list
    # Iterate over all pairs of nodes in the clique
    for i in range(len(clique)):
        for j in range(i + 1, len(clique)):
            node1 = clique_list[i]
            node2 = clique_list[j]
            # Check if there is no edge between the pair of nodes
            if adj_matrix[node1][node2] != 1:
                return False
    return True

#########################################################################################
# 10. Verify Clique using adj_list                                                      #             
#########################################################################################
def clique_verifier_list(adj_list, clique):
    for node1 in clique:
        for node2 in clique:
            if node1 != node2 and node2 not in adj_list[node1]:
                return False
    return True