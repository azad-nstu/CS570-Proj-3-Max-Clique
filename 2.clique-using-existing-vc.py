"""
@Author: Abul Kalam Azad

"""
#########################################################################################
# MAX_CLICK SOLUTION USING EXISTING VERTEX COVER ALGORITHM. TEXTBOOK-Page-1109(3rd Ed.) #                              #
#########################################################################################

# Import Packages
import networkx as nx
import matplotlib.pyplot as plt
import datetime
from utilities import *

def find_minimum_vertex_cover(adj_matrix):
    n = len(adj_matrix)
    vertex_cover = set()  # Initialize an empty set to store the vertex cover
    edges = set()  # Initialize a set to store the remaining edges

    # Calculate the total edges and populate the set of edges
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] == 1:
                edges.add((i, j))

    # Iterate until all edges are covered
    while edges:
        u, v = edges.pop()  # Arbitrarily select an edge and remove it from the set
        vertex_cover.add(u)  # Add one endpoint of the edge to the vertex cover
        vertex_cover.add(v)  # Add the other endpoint of the edge to the vertex cover
        
        # Remove edges incident on either u or v
        incident_edges = {(x, y) for (x, y) in edges if x == u or x == v or y == u or y == v}
        edges -= incident_edges  # Remove the incident edges from the set of remaining edges
    return vertex_cover


if __name__ == "__main__":
    
    def select_input_file():
        print("\nChoose an input file for 2.clique-using-existing-vc:")
        print("============================================================")
        print("1. input/Q4V10.adjlist")
        print("2. input/Q15V100.adjlist")
        print("3. input/Q30V400.adjlist")
        print("4. input/Q45V700.adjlist")
        print("5. input/Q60V1000.adjlist")
        print("6. input/G250.adjlist")
        print("7. input/G1000.adjlist")
        print("8. input/G3000.adjlist")
        print("9. input/G6000.adjlist")
        print("10. input/G16000.adjlist")

        choice = input("\nEnter the number of the input file you want to run: ")
        file_choices = {
            "1": "input/Q4V10.adjlist",
            "2": "input/Q15V100.adjlist",
            "3": "input/Q30V400.adjlist",
            "4": "input/Q45V700.adjlist",
            "5": "input/Q60V1000.adjlist",
            "6": "input/G250.adjlist",
            "7": "input/G1000.adjlist",
            "8": "input/G3000.adjlist",
            "9": "input/G6000.adjlist",
            "10": "input/G16000.adjlist"
        }

        if choice in file_choices:
            return file_choices[choice]
        else:
            print("Invalid choice. Please choose a valid option.")
            return select_input_file()

    filename = select_input_file()
    adj_matrix= lower_list_complete_matrix(filename)

    # Draw the graph
    #nodes_position = draw_graph(adj_matrix)
    complement_adj_matrix = complement_graph(adj_matrix)
    # Draw the complement graph
    #draw_graph(complement_adj_matrix)
    start_time = datetime.datetime.now()
    # Find and print the minimum vertex cover
    minimum_vertex_cover = find_minimum_vertex_cover(complement_adj_matrix)

    # Calculate the clique. Clique of G = G.V - VC of G'
    nodes = set(range(len(adj_matrix)))
    clique = (nodes - minimum_vertex_cover)
    print("\n\nSolution for {} is:".format(filename))
    print("\n===========================================")
    print("Clique:", clique)
    print("Clique Size:", len(nodes - minimum_vertex_cover))

    if clique_verifier(adj_matrix, clique):
        print("\nThe clique is correct.\n")
    else:
        print("\nThe clique is not correct.\n")
    end_time = datetime.datetime.now()
    execution_time = end_time - start_time
    hours, remainders = divmod(execution_time.total_seconds(), 3600)
    minutes, seconds = divmod(remainders, 60)
    milliseconds = execution_time.microseconds // 1000  # Convert microseconds to milliseconds

    # Print the execution time
    print("Execution Time: {} Hours, {} Minutes, {} Seconds, and {} Milliseconds\n".format(int(hours), int(minutes), int(seconds), milliseconds))      
    