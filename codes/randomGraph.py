import networkx as nx
import graphviz
import os
import random
from codes.algorithm import Floyd
from ioProcess import generateRandomGraph, renderGraph


if __name__ == '__main__':
    G = generateRandomGraph(10, 0.3)
    renderGraph(G)
    dict = Floyd(G)
    print(dict)
