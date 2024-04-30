# CS570-Proj-1-Max-Clique

#########################################################################
	=> Project Goals:													
#########################################################################
This project aims to implement Maxclique solutions using-
1. Brute force approach
2. Existing Vertex cover approach- Ref book-Page-1109(3rd Ed.)
3. Proposed Algorithms- For this, I tried many approaches with minimal to large variations. Some of them are included here:

#########################################################################
	=> Included files:													
#########################################################################
- It includes the implementation of Maxclique using brute force approach, using existing vertex cover, and some proposed approaches that are listed below:
	- clique-using-brute-force.py
	- clique-using-existing-vc.py
	- clique-using-proposed-alg-1.py
	- clique-using-proposed-alg-2.py
	- clique-using-proposed-alg-3.py
	- clique-using-proposed-alg-4.py

- Also, it includes:
	- utilities.py 		# It contains the definition of many functions that used by the algorithm implementations
	
- In addition, it has some input files in the input directory with different graph sizes:
    - Q4V10.adjlist
    - Q15V100.adjlist
    - Q30V400.adjlist
    - Q45V700.adjlist
    - Q60V1000.adjlist
    - G250.adjlist
    - G1000.adjlist
    - G3000.adjlist
    - G6000.adjlist
    - G16000.adjlist

- Finally, it has an output file:
	- output.txt		# Some outputs for different graphs are included here

#########################################################################
	=> To execute any program in this directory:						
#########################################################################
	- Just run the program-
	- It will show the option to choose any input file from a list, choose one.
	- Proposed algorithms(2-3) will ask you to provide the number of rounds that you want to run the algorithm with the hope of getting a better answer.
	- The best result would be achieved for the number of rounds = number of nodes. So, if the graph is small or if you have time, try to choose a big one.
	- Proposed algorithm-4 will ask you whether you are interested in applying a kind of backtracking or not.
	- That's it. You are good to go...
	
#########################################################################
	=> A brief introduction of the algorithms are presented below:		
#########################################################################

clique-using-brute-force.py:
================================
- For maxclique using brute force, every combination of nodes needs to test whether they all are connected to each other.
- Since we are looking for finding Maxclique, I started testing for larger combinations first to check if it could form a clique. 
- Once a clique is found, the program could stop checking remaining combinations.

clique-using-existing-vc.py:
================================
We know that Clique of G = (Vertices of G) - (VC of G')
So first we find the VC on G'.
	- Select an arbitrary edge from edge_list
	- add both vertices in the VC
	- remove all edges incident on either any or both endpoints of the arbitrary edges.
	- repeat the process until there is any edge.
	- return the VC
Now, we can get the Clique of G by removing the VC nodes from all nodes.

clique-using-proposed-alg-1.py:
================================
	- A simple variation of clique-using-existing-vc.py where instead of adding two endpoints of en edge into VC, endpoint with a higher degree added and removes associate edges.
	- Repeat the process until there is any edge to consider.

clique-using-proposed-alg-2.py:
================================
Its another variation of clique-using-existing-vc.py. It also solves clique problems by using VC on G'. 
	- Here, instead of randomly selecting edges, first, edge priority was calculated based on the number of connecting nodes on both endpoints of each edge.
	- Then, an edge is selected randomly from a certain percentage of priority edges.
	- Then, for the selected edge, which endpoint has a higher number of connecting has been selected to add in VC.
	- After that, remove all the connecting edges with the selected endpoints.
	- Then, recalculate the percentage of edges for the remaining edges.
	- Repeat the process until the remaining edge becomes empty.
	- Finally, remove the VC nodes from the G nodes to get the clique for G.


clique-using-proposed-alg-3.py:
================================
	- Initialize a clique node based on the priority from a percentage of top-ordered nodes.
	- Generate the neighbor set from the initially selected clique node. If the length of the neighbor set is greater than the so-far-formed clique size, perform the below steps.
	- For each neighbor node, count the number of edges it has with other nodes in the neighbor set and sort the neighbors accordingly.
	- Now, select a neighbor one by one from the sorted neighbor set to check if it could be added to an existing clique. If so, add it. In either case, remove it from the neighbor list.
	- Repeat the process for each node in the neighbor set. 
	- At the end, we will get the max clique for the initially selected nodes.
	- Repeat the process for several rounds to start with other initial clique nodes from the percentage of top-ordered nodes.
	- After finishing a number of rounds, return the Maxclique.

clique-using-proposed-alg-4.py:
================================
	- Initialize a clique node randomly from a percentage of top-ordered nodes.
	- Generate the neighbor set from the initially selected clique node. If the length of the neighbor set is greater than the so-far-formed clique size, perform the below steps.
	- Temporarily assume a neighbor node with the existing clique node, and count the score of that neighbor based on the number of remaining neighbor nodes that has a connection with all the nodes in temporarily formed clique nodes.
	- Do it for all the neighbor nodes, and the neighbor node with the highest score wins the race. It also adds the nodes into the remove list that cannot contain the clique property. 
	- Highest scored neighbor was added to the existing clique and both highest scored node and removed list nodes were removed from the neighbor list.
	- Repeat the process until the neighbor list becomes empty and then we get the clique for this round.
	- Now if we enable backtracking, the generated clique for each round is processed by perform_backtracking().
			- This unction temporarily removes a node from the clique to see removing that node allows more than one node to join the clique. 
			- If so, remove that node and add other nodes that could join.
			- Repeat this for all the nodes in the clique.
	- Continue the steps for some rounds.
	- Finally, the maxclique among all the rounds returned.

N.B: If you have any questions, or suggestions, please do not hesitate to contact me.
