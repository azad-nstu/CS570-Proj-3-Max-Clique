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
- It includes the implementation of Maxclique using brute force approach, using existing vertex cover and some proposed approaches that are listed below:
	- clique-using-brute-force.py
	- clique-using-existing-vc.py
	- clique-using-proposed-alg-1.py
	- clique-using-proposed-alg-2.py
	- clique-using-proposed-alg-3.py
	- clique-using-proposed-alg-4.py

- Also, it includes:
	- utilities.py 		# It contains the definition of many function that used by the algorithm implementations
	
- In addition, it has some input files in the input directory with different graph sizes like:
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
	- output.txt		# some outputs for different graphs are included here

#########################################################################
	=> To execute any program in this directory:						
#########################################################################
	- Just run the program-
	- It will show the option to choose any input file from a list, choose one.
	- Proposed algorithms(2-3) will ask you to provide the number of rounds that you want to run the algorithm with the hope of getting better answer.
		- Best result would achieve for number of rounds = number of nodes. So, if the graph is small or if you have time, try to choose a big one.
	- Proposed algorithm-4 will ask you whether you are interested to apply a kind of backtracking or not.
	- That's it. You are good to go....
	
#########################################################################
	=> A brief introduction of the algorithms are presented below:		
#########################################################################

clique-using-brute-force.py:
================================
- For maxclique using brute force, every combination of nodes need to test whether they all are connected each other.
- Since, we are looking for finding Maxclique, I started testing for larger sized combination first to check if it could form a clique. 
- Once a clique found, the program could stop checking remaining combinations.

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
	- A simple variation of clique-using-existing-vc.py where instead of adding two endpoints of en edge into VC, endpoint with higher degree added and remove associate edges.
	- Repeat the process until there have any edge to conside.

clique-using-proposed-alg-2.py:
================================
Its another variation of clique-using-existing-vc.py. It also solves clique problem by using VC on G'. 
	- Here, instead of randomly selecting edges, first, edge priority were calculated based on the number of connecting nodes on both endpoint of each edge.
	- Then, an edge selected randomly from a certain percentage of priority edges.
	- Then, for the selected edge, which endpoint has higher number of connecting has selected to add in VC.
	- After that, remove all the connecting edges with the selected endpoints.
	- Then, recalculate the percentage of edges for remaining edges.
	- Repeat the process until remaining edge becomes empty.
	- Finally, remove the VC nodes from the G nodes to get the clique for G.


clique-using-proposed-alg-3.py:
================================
	- Initialize a clique node based on the priority from a percentage of top ordered nodes.
	- Generate the neighbor set from initially selected clique node. If the length of neighbor set is greater than so far formed clique size, perform below steps.
	- For each neighbor nodes, count the number of edges it has with other nodes in the neighbor set and sort the neighbors accordingly.
	- Now, select a neighbor one by one from sorted neighbor set to check if it could be added with existing clique. If so, add it. In either cases, remove it from neighbor list.
	- Repeat the process for each node in the neighbor set. 
	- At the end we will get the maxclique for the initially sected nodes.
	- Repeat the process for a number of round to start with other initial clique nodes from the percentage of top ordered nodes.
	- After finishing a number of round, return the Maxclique.

clique-using-proposed-alg-4.py:
================================
	- Initialize a clique node randomly from a percentage of top ordered nodes.
	- Generate the neighbor set from initially selected clique node. If the length of neighbor set is greater than so far formed clique size, perform below steps.
	- Temporarily assume a neighbor node with the existing clique node,and count the score of that neighbor based on the number of remaining neighbor nodes that has a connection with all the nodes in temporarily formed clique nodes.
	- Do it for all the neighbor nodes, and the neighbor node with highest score win the race. It also add the nodes into remove list that cannot cantain the clique property. 
	- Highest scored neighbor added to the existing clique and both highest scored node and remove list nodes removed from the neighbor list.
	- Repeat the process until neighbor list becomes empty and then we get the clique for this round.
	- Now if we enable backtracking, the generated clique for each round processed by perform_backtracking().
			- This unction teporarily remove a node from the clique to see removing that node allow more than one node to join the clique. 
			- If so, remove that node and add other nodes that could join.
			- Repeat this for all the nodes in the clique.
	- Continue the steps for a number of rounds.
	- Finally, the maxclique among all the rounds returned.

N.B: If you have any questions, suggestions, please do not hesitate to contact me.
