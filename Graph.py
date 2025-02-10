from utils.country_mapper import indexer  # not used 
import networkx as nx
import matplotlib.pyplot as plt
from utils.countries import countries
from utils.cities import cities





class GenericGraph:
    def __init__(self, graph_type, directed=True, nodes=None):
        self.graph_type = graph_type
        if nodes is not None:
            self.nodes = nodes
        else:
            self.nodes = self.load_nodes(graph_type)
        self.node_to_id, self.id_to_node = self.indexer(self.nodes)
        if directed:
            self.graph = nx.DiGraph()
        else: 
            self.graph = nx.Graph()
        self.graph.add_nodes_from(self.nodes)
        self.create_graph()
        # Maintain visited, not visited status for every node 
        self.visited = {node: 0 for node in self.nodes}
        
    def load_nodes(self, graph_type):
        if graph_type == "country":
            return countries 
        elif graph_type == "city":
            return cities  
        elif graph_type == "both": 
            return countries + cities
        else:
            raise ValueError(f"{graph_type}Invalid graph type. Choose from 'country', 'city', or 'both'.")

    def indexer(self, nodes):
        node_to_id = {node: i for i, node in enumerate(nodes)}
        id_to_node = {i: node for i, node in enumerate(nodes)}
        return node_to_id, id_to_node

    def create_graph(self):
        for node_a in self.nodes:
            last_letter = node_a[-1].lower()
            for node_b in self.nodes:
                first_letter = node_b[0].lower()
                if last_letter == first_letter and node_a != node_b:
                    self.graph.add_edge(node_a, node_b)
    #not used
    def get_node_by_id(self, id):
        return self.id_to_node.get(id)
    # not used 
    def get_id_by_node(self, node):
        return self.node_to_id.get(node)

    def draw_graph(self):
        G = self.graph
        try:
            pos = nx.nx_agraph.graphviz_layout(G, prog="neato", args="-Goverlap=scale")
        except:
            pos = nx.kamada_kawai_layout(G)  # Fallback

        plt.figure(figsize=(20, 20))
        nx.draw_networkx_nodes(G,pos,node_size=500, node_color='skyblue', alpha=0.5)
        nx.draw_networkx_edges(G,pos,edge_color='gray', alpha=0.1)
        nx.draw_networkx_labels(G,pos,font_size=9, font_weight='bold')
        plt.savefig(f"{self.graph_type}.png")

if __name__ == "__main__":
    type = input("Enter graph type: ")
    graph = GenericGraph(type)
    graph.draw_graph()

      
        


