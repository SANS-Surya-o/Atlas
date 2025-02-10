### Community detection algorithms  

Network is said to have community strucutre if it can
be divided into possibly overlapping sets of nodes such that all nodes within a set are more densely connected than with the rest of the network.   

Modulariy is the metric used to measure the quality of communities found. It compares the total number of edges within communities with respect to a random baseline.  
Finding the global maxima of modularity for a given graph is NP-hard; therfore the aglorithms use some heuristic to hopefully reach atleast a local maxima.



#### NOTE:  
1. Modularity is a metric traditionally defined for undirected graphs but networkx docs mention how the modularity function changes for dircted graphs (https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.quality.modularity.html). 
Therefore, tradtional community detection algorithms like Louvain and Leiden developed for undirected graphs, can still be applied - they still return some partition whose performance can be mesaured with a modularity meant for directed graphs. 

2. Can implement Louvain's Algorithm - would upload to my github if time permits. I Understand the basic theoretical idea behind other algorithms.





### 1. Louvain's Algorithm:
The algorithm begins with a distinct community for every node. 

Phase 1: Local moving of nodes  
Phase 2: Aggregation of the network  
Go to Phase 1 until modularity can not be increased

Exact complexity unknown - 
`O(n^2)` worst case - Say every iteration of Phase 1 decreases components by one

Observed to be much better in practice: `O(nlogn)` - corresponds to the case where number of communities approximately halve every iteration. 

Since the algorithm is heuristics based, the results will differ for every iteration. For the analysis, the algorithm was run a 100 times and the partition leading to the best modularity was chosen. 

Drawbacks of Louvain's algorithm:
1. May produce internally disconnected community, for example when a node actin as a bridge between two subcomponents within the same community is shifted to a different community.

2. Smaller communities detected early on during the algorithm execution disappear with the progress of the algorithm

### 2. Leiden's Algorithm 
Source: https://en.wikipedia.org/wiki/Leiden_algorithm 

Addresses both the problems discussed above by adding a step for the refinement of the partition (by randomly splitting up communities). 

Produces the maximum modularity of all the algorithms considered in the lowest time. 

### WalterTrap's Algorithm 
Does not directly maximise modularity.  Based on the idea that random walks on a graph tend to stay within the same community. It uses these random walks to measure the similarity between nodes and iteratively merges similar nodes into communities.

Key Steps:

Random Walks: The algorithm performs short random walks on the graph.

Distance Computation: It calculates a distance between nodes based on their co-occurrence in these walks.

Hierarchical Merging: Nodes that are "close" in terms of this distance are progressively merged into larger communities.

Advantages and disadvantages:  

Hierarchical Structure: It provides a dendrogram, allowing analysis of community structures at different levels. 

Slower Execution: Higher computational complexity compared to Louvain and Leiden.



### InfoMap 
Flow based algorithm - meant for directed graphs. 



## Analysis

### InfoMap
Results:
 
9 communities: 

Community 0: The 'A' community 

Community 1: The 'S' community 

Community 2: The 'I,D,C,K' communty

Communuty 3: The 'E' community

COmmunity 4: The 'O,M' community

Communuty 5: The 'L' community

Community 6: The 'U' community

Community 7: The 'R' community

Community 8: The 'Y' community

Community 9: The 'H' community

Despite having a lower modularity score, this algorithm provides a community classification that looks
more meaningful to me.

### Others

Louvain's and Leiden's produced the following 5 communities.
5 communities:  
1. ##### The 'A' community:
Every country in this community either starts or ends with an 'a'.

2. ##### The 'N' community:
Most countries in this community either start or end with an 'n'.

3. ##### The 'S' community
Every country in this community either starts or ends with an 's'.

4. ##### The 'IDC' community
No stirct rule but majority of countries start or end with 'i', 'd' or 'c'.

5. ##### The other countries
---

###### WalterTrap Gave more communities than the modularity optimising greedy algorithms(Louvain's and Leiden's) - though the additonal ones are singleton. Indeed, the singleton sets of british indian ocean territory,burkina faso,jersey,paraguay,puerto rico are not strongly connected to any community, they have one edge each. Louvain included them in some community arbitarily as modularity of a node is always higer in a multinode community over being single. This is the drawback #2 of Louvain in action. While trivial here, it leads to loss of information about such outliers in larger networks.  

A striking difference between InfoMap and the other algorithms is that the Infomap does not identify a 'N' community. Nigeria is placed in the 'a' community, Niger in the 'R' community. All the '-stan' are scattered - kyrgystan in 'IDCK' community, Uzbekistan in 'U' community and so on. (Yet to explore the reason!)

`Q - You will be answering questions such as: Do the computed communities represent actual concepts or exhibit any patterns that align with human thought? `  

Likely not. The communtities are merely based on the starting and ending letters of the country names. In that sense, South Africa, Sri Lanka and Saudi Arabia are identical, though they are culturally and linguistically very different.  
It is interesting though to note how densly connected the 'a' community is. Lot of countries end with 'a' particularly the syllable '-ia'; which happens to be Latin for 'land of'. Explained by the large number of countries in Europe and all the countries they colonised and had an influence on the naming.
The 'n' community is dominated by countries ending with '-stan'.

`Q- Can we utilise this concept of choosing country names that are between or within communities to get an intuition of a “good” strategy? `

Yes. The player(say A) may use the knowledge of communities to gain advantage. When playing against a random player (say B), the likelihood that B stays within the community is higher by the very definition of communities. Therefore, using the border edges to push the opponent to a sparse community that 'A' has a good knowledge of increases the chances of victory. Likewise, A can be defensive and move to an easier community.  


















