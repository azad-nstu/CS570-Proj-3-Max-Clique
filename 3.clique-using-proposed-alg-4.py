"""
@Author: Abul Kalam Azad

"""
#########################################################################################
# MAX_CLICK SOLUTION USING PROPOSED ALGORITHM-4                                         #
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
def find_maximum_clique(adj_list, num_round, backtracking):
    adj_list_copy = copy.deepcopy(adj_list)  # Create a deep copy
    adj_list_copy2 = copy.deepcopy(adj_list)  # Create a deep copy
    existing_nodes = [node for node in adj_list_copy if node in adj_list]
    existing_max_clique_size = 1
    num_nodes = len(adj_list)

    if num_round < num_nodes:
        percentage = 30
        if percentage < ((num_round/num_nodes) * 100):
            percentage = (num_round/num_nodes) * 100

        sorted_nodes = sorted(adj_list_copy.items(), key=lambda x: len(x[1]), reverse=True)
        percent_nodes = math.ceil(len(existing_nodes) * percentage / 100)

        selected_nodes = set()
        while len(selected_nodes) < percent_nodes:
            node, _ = sorted_nodes.pop(0)
            selected_nodes.add(node)    # This selected list will use to initialize clique nodes in each round
    
    # Iterate for a number of rounds 
    for i in range(num_round):
        print("\n Round No:.......... {}".format(i+1))
        if num_round== num_nodes:
            initial_node_for_clique = i
        elif num_round < num_nodes:
            initial_node_for_clique = random.choice(list(selected_nodes))
            # print("\n {}. initial_node_for_clique: {}". format(i,initial_node_for_clique))
            selected_nodes.remove(initial_node_for_clique)
        else:
            initial_node_for_clique = random.choice(list(existing_nodes))
        neighbors_list = adj_list_copy[initial_node_for_clique]
        
        # If number of neighbors for initial_node_for_clique is less than the size of existing clique size 
        # Then dont need to find clique for that initial_node_for_clique node
        if len(neighbors_list) >= existing_max_clique_size:
            initial_clique = [initial_node_for_clique]  # Use a list instead of a set
            current_clique = find_candidate_clique(adj_list_copy, initial_clique, neighbors_list)
            # print("Current_clique after Round- {}: {}".format(i, current_clique))

            if len(current_clique) > existing_max_clique_size:
                existing_max_clique = current_clique
                existing_max_clique_size = len(current_clique)
            
            # If backtracking enabled, perform_backtracking() function try to increase the clique size
            if backtracking:
                neighbors_list = adj_list_copy2[initial_node_for_clique]
                updated_clique = perform_backtracking(adj_list_copy2, existing_max_clique, neighbors_list)

                if len(updated_clique) > existing_max_clique_size:
                    existing_max_clique = updated_clique
                    existing_max_clique_size = len(updated_clique)    

    return existing_max_clique, existing_max_clique_size

# To find candidate clique in each round
def find_candidate_clique(adj_list_copy, initial_clique, neighbors_list):
    while neighbors_list:
        next_clique_node, remove_list = find_next_clique_node(adj_list_copy, neighbors_list, initial_clique)
        if next_clique_node is not None:
            initial_clique.append(next_clique_node)
        if remove_list:
            for element in remove_list:
                if element in neighbors_list:
                    neighbors_list.remove(element)
        else:
            neighbors_list.remove(next_clique_node)
    return initial_clique

# To find next clique node to join the existing clique
# It also identify the neighbors that need removal as they won't contribute to clique
def find_next_clique_node(adj_list_copy, neighbors_list, initial_clique):
    scores = {}
    max_score = float('-inf')
    next_clique_node = None
    remove_list = []
    for neighbor in neighbors_list:
        temp_clique = initial_clique.copy()  # Make a copy of initial_clique

        all_connected = all(neighbor in adj_list_copy[node] for node in temp_clique)
        if all_connected:
            temp_clique.append(neighbor)  # Add the neighbor to the temporary clique
            remaining_list = [n for n in neighbors_list if n != neighbor]  # Exclude the current neighbor
            scores[neighbor] = sum(1 for node in remaining_list if all(node in adj_list_copy[n] for n in temp_clique))
            if scores[neighbor] > max_score:
                max_score = scores[neighbor]
                next_clique_node = neighbor
        else:
            remove_list.append(neighbor)
    return next_clique_node, remove_list

# If backtracking enabled, this function try to increase the clique size
def perform_backtracking(adj_list_copy2, existing_max_clique, neighbors_list):
    updated_clique = existing_max_clique.copy()
    for node in existing_max_clique:
        temp_clique = existing_max_clique.copy()
        temp_clique.remove(node)
        new_nodes = set()
        for neighbor in neighbors_list:
            if neighbor != node and neighbor not in temp_clique and all(neighbor in adj_list_copy2[node] for node in temp_clique):
                new_nodes.add(neighbor)
        if len(new_nodes) > 1:
            updated_clique.remove(node)  # Remove the node from the list
            updated_clique.extend(new_nodes)  # Add new nodes to the list       
    return updated_clique


if __name__ == "__main__":

    def select_input_file():
        print("\nChoose an input file for 3.clique-using-proposed-alg-4:")
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

    def get_backtracking_choice():
        choice = input("Do you want to enable backtracking? (yes/no): ")
        return choice.lower() == "yes"

    def get_num_round():
        num_round = input("Enter the number of rounds: ")
        return int(num_round)

    filename = select_input_file()
    backtracking = get_backtracking_choice()
    num_round = get_num_round()

    # Use the selected inputs for further processing
    adj_list = lower_list_complete_list(filename)

    start_time = datetime.datetime.now()
    max_clique, max_clique_size = find_maximum_clique(adj_list, num_round, backtracking)

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
