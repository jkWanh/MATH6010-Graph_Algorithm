import networkx as nx
import codes.algorithm as algo

if __name__ == '__main__':
    G = nx.nx_agraph.read_dot('data/graphs/randomGraph1')
    if isinstance(G, nx.MultiGraph):
        G = nx.Graph(G)
    elif isinstance(G, nx.MultiDiGraph):
        G = nx.DiGraph(G)

    mapping = {node: int(node) for node in G.nodes()}
    G = nx.relabel_nodes(G, mapping)
    for (u, v) in G.edges():
        G[u][v]['weight'] = int(G[u][v]['label'])
    
    # for (u, v) in G.edges():
    #     print(f'{u} -> {v}: {G[u][v]}')
    dist = algo.BellmanFoldSPFA(G, 0)
    dist2 = algo.BellmanFord(G, 0)
    print(dist)
    print('----------------BellmanFord----------------')
    print(dist2)
    