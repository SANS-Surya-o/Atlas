from Graph import GenericGraph
import random
# Simulate a game of atlas given the algorithms to 

class GameResult:
    def __init__(self, winner, country, len, nodes_visited):
        self.gameplay = nodes_visited
        self.winner = winner
        self.country = country
        self.len = len

    def __str__(self):
        return f"Winner: {self.winner}, Country: {self.country}"


def Simulator( A, B, graph_type="country",cur_country = "start"):
    """A - choice player A would make given the current country is cur_country"""
    """B - choice player B would make given the current country is cur_country"""
    graph = GenericGraph(graph_type=graph_type)
    turn = 0
    len = 0
    nodes_visited = []
    def run(A,B,turn,graph,cur_country,len=1):
        if turn==0 and cur_country != "start":
            nodes_visited.append(cur_country)
        if turn % 2 == 0 and cur_country!="start":
            next_country = A(cur_country, graph)
        else:
            next_country = B(cur_country, graph)
        if next_country == None:
            return turn, cur_country,len
        graph.visited[next_country] = 1
        # if turn % 2 == 0:
        #     print(f"A: {next_country} -> ")
        # else:
        #     print(f"B: {next_country} -> ")
        nodes_visited.append(next_country)
        return run(A,B,turn+1,graph,next_country,len+1)
    # return (1-run(A,B,turn,graph,cur_country)) % 2 , cur_country
    turn,cur,len = run(A,B,turn,graph,cur_country)
    if turn % 2 == 0:
        # print(nodes_visited)
        return GameResult(winner="B",country=cur,len=len,nodes_visited=nodes_visited)
    else:
        return GameResult(winner="A",country=cur,len=len,nodes_visited=nodes_visited)
    
