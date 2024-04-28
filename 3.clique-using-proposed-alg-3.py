"""
@Author: Abul Kalam Azad

"""
#########################################################################################
# MAX_CLICK SOLUTION USING PROPOSED ALGORITHM-3                                         #
#########################################################################################

# Import Packages
import networkx as nx
import matplotlib.pyplot as plt
import copy
import random
import math
import datetime
from utilities import *

# Iterate for number of rounds. In each round calculate Clique using VC and compare with existing clique for update.
def find_maximum_clique(adj_list, num_round):
    max_clique = set()
    existing_max_clique_size = 1
    adj_list_copy = copy.deepcopy(adj_list)  # Create a deep copy
    num_nodes = len(adj_list)
    existing_nodes = [node for node in adj_list_copy if node in adj_list]
    
    if num_round < num_nodes:
        percentage = 30
        if percentage < ((num_round/num_nodes) * 100):
            percentage = (num_round/num_nodes) * 100

        sorted_nodes = sorted(adj_list_copy.items(), key=lambda x: len(x[1]), reverse=True)
        percent_nodes = math.ceil(len(existing_nodes) * percentage / 100)

        selected_nodes = set()
        while len(selected_nodes) < percent_nodes:
            node, _ = sorted_nodes.pop(0)
            selected_nodes.add(node)
    else:
        percentage = 100
        sorted_nodes = sorted(adj_list_copy.items(), key=lambda x: len(x[1]), reverse=True)
        percent_nodes = math.ceil(len(existing_nodes) * percentage / 100)

        selected_nodes = set()
        while len(selected_nodes) < percent_nodes:
            node, _ = sorted_nodes.pop(0)
            selected_nodes.add(node)
    selected_nodes_list = list(selected_nodes) # This selected list will use to initialize clique nodes in each round
    
    for i in range(num_round):
        print("\n Round No:.......... {}".format(i+1))
        if i >= num_nodes:
            i = (i % num_nodes)

        initial_node_for_clique = selected_nodes_list[i]
        print("\n CC. initial_node_for_clique: ", initial_node_for_clique)
        unsorted_neighbors = adj_list[initial_node_for_clique]
        
        # If number of neighbors for initial_node_for_clique is less than the size of existing clique size 
        # Then dont need to find clique for that initial_node_for_clique node
        if len(unsorted_neighbors) >= existing_max_clique_size:     
            initial_clique = {initial_node_for_clique}
            # Sort neighbors by length in descending order
            neighbor_connections = count_neighbor_connections(adj_list, unsorted_neighbors)
            sorted_neighbors = sorted(neighbor_connections.items(), key=lambda x: len(x[1]), reverse=True)

            current_clique = find_candidate_clique(adj_list_copy, initial_clique, sorted_neighbors) 
        #print("\n Clique-{}. ========================================\n".format(i))

        # Update existing clique with new large clique
        if len(current_clique) > existing_max_clique_size:
            existing_max_clique = current_clique
            existing_max_clique_size = len(current_clique)
        print("Current_clique after Round- {}: {}".format(i, existing_max_clique))
    return existing_max_clique, existing_max_clique_size

# Count the number of connection each node with all its neighbor nodes
def count_neighbor_connections(adj_list, neighbors_set):
    connections = {}
    # Iterate over each node in the neighbor_set
    for node in neighbors_set:
        connections[node] = []
        # Count how many times the current neighbor is connected to the neighbors of the current node
        for other_neighbor in neighbors_set:
            if other_neighbor != node and other_neighbor in adj_list[node]:
                connections[node].append(other_neighbor)
    return connections

# For each round (if neighbor length qualify), this function calculates the candidate clique
def find_candidate_clique(adj_list_copy, initial_clique, sorted_neighbors):
    while sorted_neighbors:
        # Select the neighbor with the highest length
        selected_neighbor = sorted_neighbors[0][0]
        all_connected = all(selected_neighbor in adj_list[node] for node in initial_clique)
        if all_connected:
            initial_clique.add(selected_neighbor)

        sorted_neighbors = [(node, neighbors) for node, neighbors in sorted_neighbors if node != selected_neighbor]
    return initial_clique


if __name__ == "__main__":
    
    def select_input_file():
        print("\nChoose an input file for 3.clique-using-proposed-alg-3:")
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

    def get_num_round():
        num_round = input("Enter the number of rounds: ")
        return int(num_round)

    filename = select_input_file()
    num_round = get_num_round()

    # Use the selected inputs for further processing
    adj_list = lower_list_complete_list(filename)

    start_time = datetime.datetime.now()
    max_clique, max_clique_size = find_maximum_clique(adj_list, num_round)

    print("\n\nSolution for {} is:".format(filename))
    print("\n===========================================")
    print("\nClique:", sorted(max_clique))
    print("\nSize:", len(max_clique))
    if clique_verifier_list(adj_list, max_clique):
        print("\nThe Clique is Verified and Correct.\n")
    else:
        print("\nThe Clique is not correct.\n")

    end_time = datetime.datetime.now()
    execution_time = end_time - start_time
    hours, remainders = divmod(execution_time.total_seconds(), 3600)
    minutes, seconds = divmod(remainders, 60)
    milliseconds = execution_time.microseconds // 1000  # Convert microseconds to milliseconds

    # Print the execution time
    print("Execution Time: {} Hours, {} Minutes, {} Seconds, and {} Milliseconds\n".format(int(hours), int(minutes), int(seconds), milliseconds))

    