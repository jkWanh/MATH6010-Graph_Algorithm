import networkx as nx
import graphviz
import os
import random
from codes.algorithm import Floyd
from ioProcess import renderGraph

def generateRandomGraph(node: int, temperature: float) -> nx.Graph:
    # 生成一个随机图
    G = nx.erdos_renyi_graph(node, temperature)
    for (u,v) in G.edges():
        G[u][v]['weight'] = random.randint(1, 10)
    return G

if __name__ == '__main__':
    G = generateRandomGraph(10, 0.3)
    renderGraph(G)
    dict = Floyd(G)
    print(dict)
