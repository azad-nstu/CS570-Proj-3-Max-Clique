"""
@Author: Abul Kalam Azad

"""
#########################################################################################
# MAX_CLICK SOLUTION USING PROPOSED ALGORITHM-2                                         #
#########################################################################################

# Import Packages
import networkx as nx
import matplotlib.pyplot as plt
import copy
import random
import datetime
from utilities import *

# This function tries to extend clique further
def maximize_clique(adj_list, initial_clique):
    remaining_nodes = set(adj_list.keys()) - set(initial_clique)
    current_clique = set(initial_clique)

    # Iterate over the remaining nodes to try adding them to the clique
    for node in remaining_nodes:
        # Check if adding the current node to the clique forms a clique
        if all(node in adj_list[clique_node] for clique_node in current_clique):
            current_clique.add(node)

    return current_clique if current_clique else initial_clique  # Return initial_clique if no nodes added

# Iterate for number of rounds. In each round calculate Clique using VC and compare with existing clique for update.
def find_maximum_clique(adj_list, num_round):
    max_clique = set()
    max_clique_size = 0
    complement_adj_list = complement_graph_list(adj_list)
    for i in range(num_round):
        print("\n Round No:.......... {}".format(i+1))
        adj_list_copy = copy.deepcopy(complement_adj_list)  # Create a deep copy
        minimum_vertex_cover = find_minimum_vertex_cover(adj_list_copy)
        nodes = set(range(len(adj_list)))
        initial_clique = nodes - minimum_vertex_cover
        updated_clique = maximize_clique(adj_list, initial_clique)

        if len(updated_clique) > max_clique_size:
            max_clique = updated_clique
            max_clique_size = len(updated_clique)

    return max_clique, max_clique_size

# Function to find minimum VC on given adj_list
def find_minimum_vertex_cover(adj_list):
    number_of_nodes = len(adj_list)
    track_nodes = [0 for _ in range(number_of_nodes)]
    vertex_cover = set()
    edges = set()
    covered = set()
    # Add edges
    for u in adj_list:
        for v in adj_list[u]:
            edges.add((u, v))
    priorities = {edge: len(adj_list[edge[0]]) + len(adj_list[edge[1]]) for edge in edges}
    
    while edges:
        num_edges = len(edges)
        top_50_percent_threshold = sorted(priorities.values())[int(num_edges * 0.50)]
        # Filter edges with priority above the threshold
        top_50_percent_edges = [edge for edge, priority in priorities.items() if priority >= top_50_percent_threshold]
        # Select an edge randomly from the filtered edges
        selected_edge = random.choice(top_50_percent_edges)
        u, v = selected_edge

        if len(adj_list[u]) > len(adj_list[v]):
            vertex_cover.add(u)
            edges.remove(selected_edge)
            covered.add(u)
            for w in adj_list[u][:]:
                if w not in covered:
                    edges.discard((u, w))
                    edges.discard((w, u))
                    adj_list[w].remove(u)
                    adj_list[u].remove(w)
        else:
            vertex_cover.add(v)
            edges.remove(selected_edge)
            covered.add(v)
            for w in adj_list[v][:]:
                if w not in covered:
                    edges.discard((v, w))
                    edges.discard((w, v))
                    adj_list[w].remove(v)
                    adj_list[v].remove(w)

        # Update priorities after removing the selected edge
        priorities = {edge: len(adj_list[edge[0]]) + len(adj_list[edge[1]]) for edge in edges}
    return vertex_cover


if __name__ == "__main__":
    
    def select_input_file():
        print("\nChoose an input file for 3.clique-using-proposed-alg-2:")
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