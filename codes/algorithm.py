import numpy as np
import networkx as nx
from typing import Union

def Floyd(Graph : Union[nx.Graph, nx.DiGraph]) -> np.ndarray:
    """返回最短路矩阵, 使用Floyd算法

    Args:
        Graph (Union[nx.Graph, nx.DiGraph]): networkx.Graph / networkx.DiGraph 表示的图

    Returns:
        np.ndarray: 最短路矩阵
    """
    # 初始化
    n = len(Graph)
    dist = np.array([[float('inf') for i in range(n)] for j in range(n)])
    for i in range(n):
        dist[i][i] = 0
    for edge in Graph.edges():
        if isinstance(Graph, nx.DiGraph):
            dist[edge[0]][edge[1]] = Graph[edge[0]][edge[1]]['weight']
        else:
            dist[edge[0]][edge[1]] = Graph[edge[0]][edge[1]]['weight']
            dist[edge[1]][edge[0]] = Graph[edge[0]][edge[1]]['weight']
    # Floyd算法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def FloydGetPath(Graph : Union[nx.Graph, nx.DiGraph], start : int, end : int) -> (list, float):
    """返回最短路列表&路径长度, 使用Floyd算法

    Args:
        Graph (Union[nx.Graph, nx.DiGraph]): networkx.Graph / networkx.DiGraph 表示的图

    Returns:
        np.ndarray: 最短路矩阵
    """
    # 初始化
    n = len(Graph)
    dist = np.array([[float('inf') for i in range(n)] for j in range(n)])
    next_node = np.full((n, n), np.nan, dtype=object)
    for i in range(n):
        dist[i][i] = 0
    for edge in Graph.edges():
        if isinstance(Graph, nx.DiGraph):
            dist[edge[0]][edge[1]] = Graph[edge[0]][edge[1]]['weight']
            next_node[edge[0]][edge[1]] = (edge[1], dist[edge[0]][edge[1]])
        else:
            dist[edge[0]][edge[1]] = Graph[edge[0]][edge[1]]['weight']
            dist[edge[1]][edge[0]] = Graph[edge[0]][edge[1]]['weight']
            next_node[edge[0]][edge[1]] = (edge[1], dist[edge[0]][edge[1]])
            next_node[edge[1]][edge[0]] = (edge[0], dist[edge[1]][edge[0]])
    # Floyd算法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    shortest_dict = dist[start][end]

    # 建立路径
    if not isinstance(next_node[start][end], tuple):
        return [], float('inf')
    path = []
    while start != end:
        path.append((start, next_node[start][end][0], int(next_node[start][end][1])))
        start = next_node[start][end][0]
        
    return path, shortest_dict



def Dijkstra(Graph: Union[nx.Graph, nx.DiGraph], start: int):
    n = len(Graph)
    dist = np.array([float('inf') for _ in range(n)])
    dist[start] = 0
    visited = [False for _ in range(n)]
    
    for _ in range(n):
        min_dist = float('inf')
        u = -1
        for j in range(n):
            if not visited[j] and dist[j] < min_dist:
                u = j
                min_dist = dist[j]
        if u == -1:  # 所有可达节点已访问
            break
        visited[u] = True
        for v in range(n):
            if not visited[v]:
                edge_data = Graph.get_edge_data(u, v)
                if edge_data is not None:
                    weight = edge_data.get('weight', float('inf'))
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
    return dist

def BellmanFord(Graph: Union[nx.Graph, nx.DiGraph], start: int):
    n = len(Graph)
    dist = np.array([float('inf') for _ in range(n)])
    dist[start] = 0
    if isinstance(Graph, nx.DiGraph):
        for _ in range(n):
            for u, v in Graph.edges():
                if dist[u] + Graph[u][v]['weight'] < dist[v]:
                    dist[v] = dist[u] + Graph[u][v]['weight']
    elif isinstance(Graph, nx.Graph):
        for _ in range(n):
            for u, v in Graph.edges():
                if dist[u] + Graph[u][v]['weight'] < dist[v]:
                    dist[v] = dist[u] + Graph[u][v]['weight']
                if dist[v] + Graph[u][v]['weight'] < dist[u]:
                    dist[u] = dist[v] + Graph[u][v]['weight']
    return dist

def BellmanFoldSPFA(Graph : nx.Graph, start : int):
    # 初始化
    n = len(Graph)
    dist = np.array([float('inf') for i in range(n)])
    dist[start] = 0
    inQueue = [False for i in range(n)]
    inQueue[start] = True
    queue = [start]
    # Bellman-Fold算法
    while len(queue) > 0:
        u = queue.pop(0)
        inQueue[u] = False
        for v in range(n):
            if dist[u] + Graph[u][v]['weight'] < dist[v]:
                dist[v] = dist[u] + Graph[u][v]['weight']
                if not inQueue[v]:
                    queue.append(v)
                    inQueue[v] = True
    return dist

# if __name__ == '__main__':
#     G = nx.Graph()
#     G.add_edge(0, 1, weight=1)
#     G.add_edge(1, 2, weight=2)
#     G.add_edge(2, 3, weight=3)
#     G.add_edge(3, 0, weight=4)
#     G.add_edge(0, 2, weight=5)
#     G.add_edge(1, 3, weight=6)
#     G.add_edge(4, 5, weight=7)
#     print(BellmanFord(G, 3))