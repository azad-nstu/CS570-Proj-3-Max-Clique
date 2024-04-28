"""
@Author: Abul Kalam Azad

"""
#########################################################################################
# MAX_CLICK SOLUTION USING BRUTE FORCE ALGORITHM                                        #
#########################################################################################

# Import Packages
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
import datetime
from utilities import *

# Check each combation of nodes (from large to small) to see if its a clique. Once found, it returns.
def brute_force_max_clique(adj_matrix):
    n = len(adj_matrix)
    max_cliques = []
    max_size = 0
    for r in range(n, 0, -1):  # Check combinations from large to small size
        for nodes in combinations(range(n), r):
            if clique_verifier(adj_matrix, nodes):
                max_size = len(nodes)
                max_cliques = [nodes]
                return max_cliques, max_size  # Stop the loop and return when a clique is found
    return max_cliques, max_size


if __name__ == "__main__":
    
    def select_input_file():
        print("\nChoose an input file for 1.clique-using-brute-force:")
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
    adj_matrix = lower_list_complete_matrix(filename) # Complete adjacency matrix function
    # draw_graph(adj_matrix)

    start_time = datetime.datetime.now()
    max_clique, max_clique_size = brute_force_max_clique(adj_matrix)
    print("\n\nSolution for {} is:".format(filename))
    print("\n===========================================")
    print("Clique:", max_clique)
    print("Clique Size:", max_clique_size)
    if clique_verifier(adj_matrix, max_clique):
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