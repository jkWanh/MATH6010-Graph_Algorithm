import numpy as np
import networkx as nx
from typing import Union

def Floyd(Graph : Union[nx.Graph, nx.DiGraph]) -> np.ndarray:
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



def Floyd2(Graph : nx.Graph) -> np.ndarray:
    """返回最短路矩阵, 使用Floyd算法, 专用于无向图

    Args:
        Graph (Graph): networkx.Graph表示的图

    Returns:
        np.ndarray: 最短路矩阵
    """
    # 初始化
    n = len(Graph)
    dist = np.array([[float('inf') for i in range(n)] for j in range(n)])
    for i in range(n):
        dist[i][i] = 0
    for edge in Graph.edges():
        dist[edge[0]][edge[1]] = Graph[edge[0]][edge[1]]['weight']
        dist[edge[1]][edge[0]] = Graph[edge[0]][edge[1]]['weight']
    # Floyd算法，结果为对称矩阵因此每次只计算上三角矩阵
    for k in range(n):
        for i in range(n):
            for j in range(i, n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    dist[j][i] = dist[i][k] + dist[k][j]
    return dist

def Dijsktra(Graph : nx.Graph, start : int):
    # 初始化
    n = len(Graph)
    dist = np.array([float('inf') for i in range(n)])
    dist[start] = 0
    visited = [False for i in range(n)]
    # Dijkstra算法
    for i in range(n):
        u = -1
        for j in range(n):
            if not visited[j] and (u == -1 or dist[j] < dist[u]):
                u = j
        visited[u] = True
        for v in range(n):
            if not visited[v] and dist[u] + Graph[u][v]['weight'] < dist[v]:
                dist[v] = dist[u] + Graph[u][v]['weight']
    return dist

def BellmanFord(Graph : nx.Graph, start : int):
    # 初始化
    n = len(Graph)
    dist = np.array([float('inf') for i in range(n)])
    dist[start] = 0
    # Bellman-Ford算法
    for i in range(n):
        for edge in Graph.edges():
            if dist[edge[0]] + Graph[edge[0]][edge[1]]['weight'] < dist[edge[1]]:
                dist[edge[1]] = dist[edge[0]] + Graph[edge[0]][edge[1]]['weight']
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
