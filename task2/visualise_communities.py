import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from Graph import GenericGraph
from collections import defaultdict
from networkx.algorithms.community.quality import modularity
from cdlib import algorithms



def community_layout(g, partition):
    """
    Compute the layout for a modular graph.


    Arguments:
    ----------
    g -- networkx.Graph or networkx.DiGraph instance
        graph to plot

    partition -- dict mapping int node -> int community
        graph partitions


    Returns:
    --------
    pos -- dict mapping int node -> (float x, float y)
        node positions

    """

    pos_communities = _position_communities(g, partition, scale=3.)

    pos_nodes = _position_nodes(g, partition, scale=1.)

    # combine positions
    pos = dict()
    for node in g.nodes():
        pos[node] = pos_communities[node] + 40*pos_nodes[node]

    return pos

def _position_communities(g, partition, **kwargs):

    # create a weighted graph, in which each node corresponds to a community,
    # and each edge weight to the number of edges between communities
    between_community_edges = _find_between_community_edges(g, partition)

    communities = set(partition.values())
    hypergraph = nx.DiGraph()
    hypergraph.add_nodes_from(communities)
    for (ci, cj), edges in between_community_edges.items():
        hypergraph.add_edge(ci, cj, weight=len(edges))

    # find layout for communities
    pos_communities = nx.nx_agraph.graphviz_layout(hypergraph, prog="neato", args="-Goverlap=scale")

    # set node positions to position of community
    pos = dict()
    for node, community in partition.items():
        pos[node] = pos_communities[community]

    return pos

def _find_between_community_edges(g, partition):

    edges = dict()

    for (ni, nj) in g.edges():
        ci = partition[ni]
        cj = partition[nj]

        if ci != cj:
            try:
                edges[(ci, cj)] += [(ni, nj)]
            except KeyError:
                edges[(ci, cj)] = [(ni, nj)]

    return edges

def _position_nodes(g, partition, **kwargs):
    """
    Positions nodes within communities.
    """

    communities = dict()
    for node, community in partition.items():
        try:
            communities[community] += [node]
        except KeyError:
            communities[community] = [node]

    pos = dict()
    for ci, nodes in communities.items():
        subgraph = g.subgraph(nodes)
        pos_subgraph = nx.spring_layout(subgraph,k=30,**kwargs)
        # pos_subgraph = nx.nx_agraph.graphviz_layout(subgraph, prog="neato", args="-Goverlap=scale")
        pos.update(pos_subgraph)

    return pos




   
def visualise_communities( g, partition, file_name=None ):
    partition_index = defaultdict(int)
    set_index = 0
    for com in partition:
        print(f'Community {set_index}:')
        for country in com:
            print(f'\t{country}')
            partition_index[country] = set_index
        set_index += 1
    node_colors = []
    for node in g.nodes():
        node_colors.append(partition_index[node])

    plt.figure(figsize=(30, 30))
    pos = community_layout(g, partition_index)
    # nx.draw(g, pos, node_color=list(partition_index.values()), with_labels=True, font_weight="bold",  alpha=0.3, width=0.2)
    nx.draw_networkx_edges(g, pos, edge_color='gray', width=0.5, alpha=0.5)
    nx.draw_networkx_nodes(g, pos, node_color=node_colors, alpha=0.5, node_size=500)
    nx.draw_networkx_labels(g, pos, font_weight="bold")
    if file_name is not None:
        plt.savefig(file_name)

def InfoMap():
    g = GenericGraph(graph_type="country").graph
    nc = algorithms.infomap(g)
    communities = [set(c) for c in nc.communities]
    print(modularity(g, communities))
    visualise_communities(g, communities)

if __name__== "__main__":
    InfoMap()